from django.shortcuts import render, redirect
from vendorapp.models import Multivendors, Userreg, Fooditems, Cart,Franchise
from vendorapp.forms import MultivendorsForm, VendorUserForm, UserregForm, FooditemsForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, get_object_or_404


def regvendor(request):
    registered = False

    if request.method == "POST":
        vendor_form = MultivendorsForm(request.POST, request.FILES)
        user_form = VendorUserForm(request.POST)

        if vendor_form.is_valid() and user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            vendor = vendor_form.save(commit=False)
            vendor.user = user
            vendor.save()

            registered = True

        else:
            print(user_form.errors, vendor_form.errors)

    else:
        vendor_form = MultivendorsForm()
        user_form = VendorUserForm()

    return render(request, 'vendors/regvendor.html', {
        'vendor_form': vendor_form,
        'user_form': user_form,
        'registered': registered
    })


def reguser(request):
    registered = False

    if request.method == "POST":
        user_form = UserregForm(request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            # Create user profile in Userreg model
            Userreg.objects.create(user=user)

            registered = True
            return redirect('login')

    else:
        user_form = UserregForm()

    return render(request, 'vendors/reguser.html', {
        'user_form': user_form,
        'registered': registered
    })


def login(request):
    error = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("homepage")
        else:
            error = "Invalid username or password!"

    return render(request, "vendors/login.html", {"error": error})


def logout(request):
    auth_logout(request)
    return redirect('login')


@login_required(login_url='login')
def homepage(request):
    return render(request, 'vendors/homepage.html')


@login_required(login_url='login')
def dashboard(request):

    logged_user = request.user

    # Check if vendor exists
    vendor = Multivendors.objects.filter(user=logged_user).first()

    if vendor:
        role = "vendor"
        data = vendor

    else:
        user_details = Userreg.objects.filter(user=logged_user).first()

        if user_details:
            role = "user"
            data = user_details
        else:
            role = "unknown"
            data = None

    vendors = Multivendors.objects.all()

    return render(request, 'vendors/dashboard.html', {
        "role": role,
        "data": data,
        "user": request.user,
        "forms": vendors
    })


@login_required(login_url='login')
def hoteldetail(request, id):
    vendor = get_object_or_404(Multivendors, id=id)
    food_items = Fooditems.objects.filter(vendor=vendor)

    logged_user = request.user

    # ROLE CHECK
    role = "vendor" if Multivendors.objects.filter(user=logged_user).exists() else "user"

    # ✅ FRANCHISE ACCEPTED (CORRECT WAY)
    franchise_accepted = (
        vendor.franchise is True and vendor.user == logged_user
    )

    user_details = None
    emi_details = None

    if franchise_accepted:
        # USER DETAILS
        user_details = {
            "name": logged_user.get_full_name() or logged_user.username,
            "email": logged_user.email,
        }

        # GET FRANCHISE CONFIG (NO accepted / user here)
        franchise = vendor.franchises.first()

        if franchise:
            emi_details = {
                "total_investment": franchise.total_investment,
                "agreement_years": franchise.aggr_years,
                "profit_sharing": franchise.profit_sharing,
            }

    return render(request, 'vendors/hoteldetail.html', {
        'vendor': vendor,
        'food_items': food_items,
        'role': role,
        'franchise_accepted': franchise_accepted,
        'user_details': user_details,
        'emi_details': emi_details,
    })


@login_required(login_url='login')
def add_menu(request, id):
    vendor = get_object_or_404(Multivendors, id=id)

    if request.method == "POST":
        form = FooditemsForm(request.POST, request.FILES)
        if form.is_valid():
            food_item = form.save(commit=False)
            food_item.vendor = vendor
            food_item.save()
            return redirect('dashboard')
    else:
        form = FooditemsForm()

    return render(request, 'vendors/add_menu.html', {'vendor': vendor, 'form': form})


@login_required(login_url='login')
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)

    total_price = sum(ci.item.item_price * ci.quantity for ci in cart_items)

    return render(request, 'vendors/view_cart.html', {
        "cart_items": cart_items,
        "total_price": total_price
    })


@login_required(login_url='login')
def add_to_cart(request, item_id):
    user = request.user
    item = get_object_or_404(Fooditems, id=item_id)

    cart_item, created = Cart.objects.get_or_create(
        user=user,
        item=item
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('view_cart')


@login_required(login_url='login')
def remove_from_cart(request, item_id):
    user = request.user
    item = get_object_or_404(Fooditems, id=item_id)

    cart_item = Cart.objects.filter(user=user, item=item).first()

    if cart_item:
        cart_item.delete()

    return redirect('view_cart')

@login_required(login_url='login')
def franchise_details(request, id):
    vendor = Multivendors.objects.get(id=id)

    vendor_details = {
        "Restaurant Name": vendor.restaurant_name,
        "Address": vendor.address,
        "City": vendor.city,
        "State": vendor.state,
        "Zip Code": vendor.zip_code,
    }

    franchise = vendor.franchises.first()
    if franchise:
        franchise_details = {
            "Total Investment": franchise.total_investment,
            "Agreement Years": franchise.aggr_years,
            "Profit Sharing (%)": franchise.profit_sharing,
            "Description": franchise.description,
        }
    else:
        franchise_details = None  # no franchise

    return render(request, "vendors/franchise_details.html", {
        "vendor": vendor,
        "vendor_details": vendor_details,
        "franchise_details": franchise_details
    })

@login_required(login_url='login')
def emicalculation(request, id):
    vendor = get_object_or_404(Multivendors, id=id)
    franchise = vendor.franchises.first()

    emi = None
    error = None
    interest_rate = None
    years = None

    if request.method == "POST":
        loan_amount = float(request.POST.get("loan_amount"))
        years = int(request.POST.get("years"))

        total_investment = float(franchise.total_investment)

        # ✅ Validation: Loan must be less than investment
        if loan_amount >= total_investment:
            error = "Loan amount must be less than total investment."
        else:
            # ✅ Interest rate logic
            if years == 1:
                interest_rate = 13
            elif years == 2:
                interest_rate = 11
            elif years == 5:
                interest_rate = 10
            elif years == 7:
                interest_rate = 9
            elif years == 10:
                interest_rate = 8
            else:
                error = "EMI available within 10 years."

        if not error:
            monthly_rate = interest_rate / (12 * 100)
            months = years * 12

            emi = (loan_amount * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
            emi = round(emi, 2)

    return render(request, 'vendors/emi_calci.html', {
        'vendor': vendor,
        'franchise': franchise,
        'emi': emi,
        'error': error,
        'years':years,
        'interest_rate': interest_rate
    })
