import '/backend/api_requests/api_calls.dart';
import '/flutter_flow/flutter_flow_util.dart';
import 'carrello_widget.dart' show CarrelloWidget;
import 'package:flutter/material.dart';

class CarrelloModel extends FlutterFlowModel<CarrelloWidget> {
  ///  State fields for stateful widgets in this page.

  // Stores action output result for [Backend Call - API (view carrello)] action in ListView widget.
  ApiCallResponse? risultato;
  // Stores action output result for [Backend Call - API (rimuovi dal carrello)] action in Text widget.
  ApiCallResponse? rimuoviCarrello;
  // Stores action output result for [Backend Call - API (ordine mobile)] action in Button widget.
  ApiCallResponse? ordineMobile;
  // Stores action output result for [Backend Call - API (conferma ordine)] action in Button widget.
  ApiCallResponse? ordineNegozio;

  @override
  void initState(BuildContext context) {}

  @override
  void dispose() {}
}
