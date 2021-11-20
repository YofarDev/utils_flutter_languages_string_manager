import 'languages.dart';

class LanguageEn extends Languages {

///  Global  ///
@override
String get appName => "My beautiful app";
@override
String get errorTryAgain => "A problem happened, try again later";

///  Login Page  ///
@override
String get loginTitle => "Log in";
@override
String get registerTxt => "Sign-up free!";
@override
String get username => "Username";
@override
String get email => "Email";
@override
String get password => "Password";
@override
String get login => "Login";
@override
String get register => "Create an account";
@override
String get processing => "Loading...";
@override
String get confirm => "Confirm";
@override
String get forgotPassword => "Forgot your password?";
@override
String get whoAreWe => "Who are we ?";
@override
String get facebookLogin => "Continue with Facebook";
@override
String get googleLogin => "Continue with Google";
@override
String get alreadyAccount => "Already an account?";

///  Login errors ///
@override
String get errorEmail => "Type your email address";
@override
String get errorPassword => "Type a password with at least 6 characters";
@override
String get incorrectPassword => "Wrong password";
@override
String get errorEmailFormat => "This email is badly formated";
@override
String get errorSignInNoUser => "No account found for this email";
@override
String get errorSignInWrongPassword => "This password is incorrect";
@override
String get errorEmailDisabled => "User with this email has been disabled.";
@override
String get errorTooManyRequests => "Too many requests. Try again later.";
@override
String get errorOperationNotEnabled => "Signing in with Email and Password is not enabled.";

}