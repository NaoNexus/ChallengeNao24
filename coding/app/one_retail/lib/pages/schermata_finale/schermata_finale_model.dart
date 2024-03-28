import '/flutter_flow/flutter_flow_util.dart';
import 'schermata_finale_widget.dart' show SchermataFinaleWidget;
import 'package:flutter/material.dart';

class SchermataFinaleModel extends FlutterFlowModel<SchermataFinaleWidget> {
  ///  State fields for stateful widgets in this page.

  final unfocusNode = FocusNode();

  @override
  void initState(BuildContext context) {}

  @override
  void dispose() {
    unfocusNode.dispose();
  }
}
