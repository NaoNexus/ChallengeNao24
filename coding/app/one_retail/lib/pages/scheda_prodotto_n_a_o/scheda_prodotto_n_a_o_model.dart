import '/backend/api_requests/api_calls.dart';
import '/flutter_flow/flutter_flow_util.dart';
import 'scheda_prodotto_n_a_o_widget.dart' show SchedaProdottoNAOWidget;
import 'package:flutter/material.dart';

class SchedaProdottoNAOModel extends FlutterFlowModel<SchedaProdottoNAOWidget> {
  ///  State fields for stateful widgets in this page.

  final unfocusNode = FocusNode();
  // Stores action output result for [Backend Call - API (aggiungi al carrello)] action in Button widget.
  ApiCallResponse? aggiungialcarrello;
  // Stores action output result for [Backend Call - API (Descrizione NAO)] action in FloatingActionButton widget.
  ApiCallResponse? risultato;

  @override
  void initState(BuildContext context) {}

  @override
  void dispose() {
    unfocusNode.dispose();
  }
}
