import '/backend/api_requests/api_calls.dart';
import '/flutter_flow/flutter_flow_util.dart';
import 'n_a_owait_widget.dart' show NAOwaitWidget;
import 'package:flutter/material.dart';

class NAOwaitModel extends FlutterFlowModel<NAOwaitWidget> {
  ///  Local state fields for this page.

  String fotoURL = '0';

  ///  State fields for stateful widgets in this page.

  final unfocusNode = FocusNode();
  // Stores action output result for [Backend Call - API (inizia dialogo)] action in NAOwait widget.
  ApiCallResponse? risultato;

  @override
  void initState(BuildContext context) {}

  @override
  void dispose() {
    unfocusNode.dispose();
  }
}
