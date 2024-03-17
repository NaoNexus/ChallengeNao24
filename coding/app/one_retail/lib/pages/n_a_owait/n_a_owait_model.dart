import '/backend/api_requests/api_calls.dart';
import '/flutter_flow/flutter_flow_util.dart';
import '/flutter_flow/instant_timer.dart';
import 'n_a_owait_widget.dart' show NAOwaitWidget;
import 'package:flutter/material.dart';

class NAOwaitModel extends FlutterFlowModel<NAOwaitWidget> {
  ///  State fields for stateful widgets in this page.

  final unfocusNode = FocusNode();
  // Stores action output result for [Backend Call - API (inizia dialogo)] action in NAOwait widget.
  ApiCallResponse? apiResulturg;
  InstantTimer? instantTimer;

  /// Initialization and disposal methods.

  @override
  void initState(BuildContext context) {}

  @override
  void dispose() {
    unfocusNode.dispose();
    instantTimer?.cancel();
  }

  /// Action blocks are added here.

  /// Additional helper methods are added here.
}
