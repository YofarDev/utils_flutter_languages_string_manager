import 'languages.dart';

class LanguageFr extends Languages {

///  Global  ///
@override
String get appName => "Ma jolie application";
@override
String get errorTryAgain => "Un problème est survenu, essaye encore!";

///  Login Page  ///
@override
String get loginTitle => "Se connecter";
@override
String get registerTxt => "Inscrivez vous gratuitement!";
@override
String get username => "Identifiant";
@override
String get email => "Email";
@override
String get password => "Mot de passe";
@override
String get login => "Se connecter";
@override
String get register => "Créer un compte";
@override
String get processing => "Chargement...";
@override
String get confirm => "Confirmer";
@override
String get forgotPassword => "Mot de passe oublié";
@override
String get whoAreWe => "Qui sommes nous ?";
@override
String get facebookLogin => "Continuer avec Facebook";
@override
String get googleLogin => "Continuer avec Google";
@override
String get alreadyAccount => "Déjà un compte?";

///  Login errors ///
@override
String get errorEmail => "Entrez votre adresse email";
@override
String get errorPassword => "Entrez un mot de passe avec au moins 6 caractères";
@override
String get incorrectPassword => "Mot de passe incorrect";
@override
String get errorEmailFormat => "Cet email n'est pas au bon format";
@override
String get errorSignInNoUser => "Aucun compte avec cet email trouvé";
@override
String get errorSignInWrongPassword => "Ce mot de passe est incorrect";
@override
String get errorEmailDisabled => "User with this email has been disabled.";
@override
String get errorTooManyRequests => "Too many requests. Try again later.";
@override
String get errorOperationNotEnabled => "Signing in with Email and Password is not enabled.";

}