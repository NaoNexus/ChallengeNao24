import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import 'package:flutter/material.dart';
import 'schermata_finale_model.dart';
export 'schermata_finale_model.dart';

class SchermataFinaleWidget extends StatefulWidget {
  const SchermataFinaleWidget({super.key});

  @override
  State<SchermataFinaleWidget> createState() => _SchermataFinaleWidgetState();
}

class _SchermataFinaleWidgetState extends State<SchermataFinaleWidget> {
  late SchermataFinaleModel _model;

  final scaffoldKey = GlobalKey<ScaffoldState>();

  @override
  void initState() {
    super.initState();
    _model = createModel(context, () => SchermataFinaleModel());
  }

  @override
  void dispose() {
    _model.dispose();

    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () => _model.unfocusNode.canRequestFocus
          ? FocusScope.of(context).requestFocus(_model.unfocusNode)
          : FocusScope.of(context).unfocus(),
      child: Scaffold(
        key: scaffoldKey,
        backgroundColor: FlutterFlowTheme.of(context).primaryBackground,
        body: SafeArea(
          top: true,
          child: Align(
            alignment: const AlignmentDirectional(0.0, 0.0),
            child: Column(
              mainAxisSize: MainAxisSize.max,
              mainAxisAlignment: MainAxisAlignment.start,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                ClipRRect(
                  borderRadius: BorderRadius.circular(8.0),
                  child: Image.asset(
                    'assets/images/OneRetail_logo.png',
                    width: 300.0,
                    height: 60.0,
                    fit: BoxFit.fitWidth,
                  ),
                ),
                Column(
                  mainAxisSize: MainAxisSize.max,
                  children: [
                    Text(
                      'Procedi con il pagamento in cassa.',
                      style: FlutterFlowTheme.of(context).bodyMedium,
                    ),
                    Text(
                      'Ti ringraziamo per aver utilizzato OneRetail!',
                      style: FlutterFlowTheme.of(context).bodyMedium,
                    ),
                  ],
                ),
                Row(
                  mainAxisSize: MainAxisSize.max,
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Text(
                      'Com\'è andata? Appreziamo il tuo ',
                      style: FlutterFlowTheme.of(context).bodyMedium,
                    ),
                    InkWell(
                      splashColor: Colors.transparent,
                      focusColor: Colors.transparent,
                      hoverColor: Colors.transparent,
                      highlightColor: Colors.transparent,
                      onTap: () async {
                        await launchURL(
                            'https://form.jotform.com/233373223897059');
                      },
                      child: Text(
                        'feedback',
                        style: FlutterFlowTheme.of(context).bodyMedium.override(
                              fontFamily: 'Readex Pro',
                              color: FlutterFlowTheme.of(context).secondaryText,
                              decoration: TextDecoration.underline,
                            ),
                      ),
                    ),
                    Text(
                      '!',
                      style: FlutterFlowTheme.of(context).bodyMedium,
                    ),
                  ],
                ),
              ]
                  .divide(const SizedBox(height: 20.0))
                  .addToStart(const SizedBox(height: 100.0)),
            ),
          ),
        ),
      ),
    );
  }
}
