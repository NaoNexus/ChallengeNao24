import '/backend/api_requests/api_calls.dart';
import '/flutter_flow/flutter_flow_util.dart';
import 'q_rscan_widget.dart' show QRscanWidget;
import 'package:flutter/material.dart';

class QRscanModel extends FlutterFlowModel<QRscanWidget> {
  ///  State fields for stateful widgets in this page.

  final unfocusNode = FocusNode();
  var qr = '';
  // Stores action output result for [Backend Call - API (view prodotto qr)] action in IconButton widget.
  ApiCallResponse? qRresult;

  @override
  void initState(BuildContext context) {}

  @override
  void dispose() {
    unfocusNode.dispose();
  }
}
