import '/flutter_flow/flutter_flow_util.dart';
import 'select_experience_widget.dart' show SelectExperienceWidget;
import 'package:flutter/material.dart';

class SelectExperienceModel extends FlutterFlowModel<SelectExperienceWidget> {
  ///  State fields for stateful widgets in this page.

  final unfocusNode = FocusNode();

  @override
  void initState(BuildContext context) {}

  @override
  void dispose() {
    unfocusNode.dispose();
  }
}
