import 'package:flutter/material.dart';

abstract class Languages {
static Languages of(BuildContext context) {
return Localizations.of<Languages>(context, Languages)!;

}
///  Global  ///
String get appName;
String get errorTryAgain;

///  Login Page  ///
String get loginTitle;
String get registerTxt;
String get username;
String get email;
String get password;
String get login;
String get register;
String get processing;
String get confirm;
String get forgotPassword;
String get whoAreWe;
String get facebookLogin;
String get googleLogin;
String get alreadyAccount;

///  Login errors ///
String get errorEmail;
String get errorPassword;
String get incorrectPassword;
String get errorEmailFormat;
String get errorSignInNoUser;
String get errorSignInWrongPassword;
String get errorEmailDisabled;
String get errorTooManyRequests;
String get errorOperationNotEnabled;

}