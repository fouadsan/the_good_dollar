from django.urls import path
from django.contrib.auth import views as auth_views
from .views import dashboard_screen, get_orders, orders_screen, reviews_screen, addressbook_screen, signup_screen, profile_screen
from .forms import UserLoginForm, ResetPasswordForm, ResetPasswordConfirmForm
from django.urls import path, reverse_lazy

app_name = 'users'

urlpatterns = [
    path('dashboard/', dashboard_screen, name='dashboard'),
    path('orders_data',get_orders,name='get-orders-data'),
    path('profile/', profile_screen, name='profile'),
    path('orders/', orders_screen, name='orders'),
    path('reviews/', reviews_screen, name='reviews'),
    path('addressbok/', addressbook_screen, name='addressbook'),
    path('sign-up/', signup_screen, name='signup'),
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html',
        authentication_form=UserLoginForm,
        extra_context={'header': 'Login'}),
        name='login'
    ),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html',
                                                  extra_context={'header': 'Logout'},), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html',
             form_class=ResetPasswordForm,
             extra_context={'header': 'Password Reset'},
             success_url=reverse_lazy('users:password_reset_done')
         ),
         name='password_reset',
         ),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html',
             extra_context={'header': 'Password Reset'},
         ),
         name='password_reset_done'
         ),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html',
             form_class=ResetPasswordConfirmForm,
             extra_context={'header': 'Change your password'},
         ),
         name='password_reset_confirm'
         ),

]