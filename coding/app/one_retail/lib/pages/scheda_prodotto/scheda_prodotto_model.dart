import '/backend/api_requests/api_calls.dart';
import '/flutter_flow/flutter_flow_util.dart';
import 'scheda_prodotto_widget.dart' show SchedaProdottoWidget;
import 'package:flutter/material.dart';

class SchedaProdottoModel extends FlutterFlowModel<SchedaProdottoWidget> {
  ///  State fields for stateful widgets in this page.

  final unfocusNode = FocusNode();
  // Stores action output result for [Backend Call - API (aggiungi al carrello)] action in Button widget.
  ApiCallResponse? aggiungialcarrello;

  /// Initialization and disposal methods.

  @override
  void initState(BuildContext context) {}

  @override
  void dispose() {
    unfocusNode.dispose();
  }

  /// Action blocks are added here.

  /// Additional helper methods are added here.
}
