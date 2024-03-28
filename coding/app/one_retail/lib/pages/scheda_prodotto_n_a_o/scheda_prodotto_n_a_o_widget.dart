import '/backend/api_requests/api_calls.dart';
import '/flutter_flow/flutter_flow_icon_button.dart';
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import '/flutter_flow/flutter_flow_widgets.dart';
import '/flutter_flow/custom_functions.dart' as functions;
import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:provider/provider.dart';
import 'scheda_prodotto_n_a_o_model.dart';
export 'scheda_prodotto_n_a_o_model.dart';

class SchedaProdottoNAOWidget extends StatefulWidget {
  const SchedaProdottoNAOWidget({
    super.key,
    required this.id,
  });

  final int? id;

  @override
  State<SchedaProdottoNAOWidget> createState() =>
      _SchedaProdottoNAOWidgetState();
}

class _SchedaProdottoNAOWidgetState extends State<SchedaProdottoNAOWidget> {
  late SchedaProdottoNAOModel _model;

  final scaffoldKey = GlobalKey<ScaffoldState>();

  @override
  void initState() {
    super.initState();
    _model = createModel(context, () => SchedaProdottoNAOModel());
  }

  @override
  void dispose() {
    _model.dispose();

    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    context.watch<FFAppState>();

    return GestureDetector(
      onTap: () => _model.unfocusNode.canRequestFocus
          ? FocusScope.of(context).requestFocus(_model.unfocusNode)
          : FocusScope.of(context).unfocus(),
      child: Scaffold(
        key: scaffoldKey,
        backgroundColor: FlutterFlowTheme.of(context).secondaryBackground,
        floatingActionButton: Align(
          alignment: const AlignmentDirectional(1.0, -1.0),
          child: Padding(
            padding: const EdgeInsetsDirectional.fromSTEB(0.0, 85.0, 0.0, 0.0),
            child: FloatingActionButton(
              onPressed: () async {
                _model.risultato = await DescrizioneNAOCall.call(
                  idOggetto: widget.id,
                );
                if ((_model.risultato?.succeeded ?? true)) {
                  await Future.delayed(const Duration(milliseconds: 1));
                } else {
                  ScaffoldMessenger.of(context).showSnackBar(
                    SnackBar(
                      content: Text(
                        'Errore',
                        style: TextStyle(
                          color: FlutterFlowTheme.of(context).primaryText,
                        ),
                      ),
                      duration: const Duration(milliseconds: 4000),
                      backgroundColor: FlutterFlowTheme.of(context).error,
                    ),
                  );
                }

                setState(() {});
              },
              backgroundColor: FlutterFlowTheme.of(context).primary,
              elevation: 8.0,
              child: Padding(
                padding: const EdgeInsetsDirectional.fromSTEB(0.0, 0.0, 4.0, 0.0),
                child: Icon(
                  FFIcons.knaoIcon,
                  color: FlutterFlowTheme.of(context).info,
                  size: 36.0,
                ),
              ),
            ),
          ),
        ),
        appBar: AppBar(
          backgroundColor: FlutterFlowTheme.of(context).primary,
          automaticallyImplyLeading: false,
          leading: FlutterFlowIconButton(
            borderColor: Colors.transparent,
            borderRadius: 30.0,
            borderWidth: 1.0,
            buttonSize: 60.0,
            icon: const Icon(
              Icons.arrow_back_ios,
              color: Colors.white,
              size: 30.0,
            ),
            onPressed: () async {
              context.pop();
            },
          ),
          title: Text(
            'Prodotto selezionato',
            style: FlutterFlowTheme.of(context).headlineMedium.override(
                  fontFamily: 'Outfit',
                  color: Colors.white,
                  fontSize: 22.0,
                  letterSpacing: 0.0,
                ),
          ),
          actions: const [],
          centerTitle: true,
          elevation: 2.0,
        ),
        body: SafeArea(
          top: true,
          child: SizedBox(
            width: double.infinity,
            height: double.infinity,
            child: Stack(
              children: [
                Align(
                  alignment: const AlignmentDirectional(0.0, -1.0),
                  child: FutureBuilder<ApiCallResponse>(
                    future: ViewProdottoCall.call(
                      id: widget.id,
                    ),
                    builder: (context, snapshot) {
                      // Customize what your widget looks like when it's loading.
                      if (!snapshot.hasData) {
                        return const Center(
                          child: SizedBox(
                            width: 50.0,
                            height: 50.0,
                            child: SpinKitFadingCube(
                              color: Colors.black,
                              size: 50.0,
                            ),
                          ),
                        );
                      }
                      final columnViewProdottoResponse = snapshot.data!;
                      return Column(
                        mainAxisSize: MainAxisSize.max,
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          // This image is pretty cool i'm trying to add this multi-line code and all sorts of cool stuff.
                          Align(
                            alignment: const AlignmentDirectional(0.0, -1.0),
                            child: Image.network(
                              functions.uRLmerge(
                                  'http://192.168.0.170:5010',
                                  getJsonField(
                                    columnViewProdottoResponse.jsonBody,
                                    r'''$.data.foto''',
                                  ).toString())!,
                              width: 300.0,
                              height: 300.0,
                              fit: BoxFit.fitWidth,
                            ),
                          ),
                          Padding(
                            padding: const EdgeInsetsDirectional.fromSTEB(
                                24.0, 4.0, 0.0, 0.0),
                            child: Text(
                              getJsonField(
                                columnViewProdottoResponse.jsonBody,
                                r'''$.data.categoria''',
                              ).toString(),
                              style: FlutterFlowTheme.of(context)
                                  .labelMedium
                                  .override(
                                    fontFamily: 'Readex Pro',
                                    letterSpacing: 0.0,
                                  ),
                            ),
                          ),
                          Padding(
                            padding: const EdgeInsetsDirectional.fromSTEB(
                                24.0, 0.0, 0.0, 0.0),
                            child: Text(
                              valueOrDefault<String>(
                                functions.capitalize(getJsonField(
                                  columnViewProdottoResponse.jsonBody,
                                  r'''$.data.titolo''',
                                ).toString()),
                                'Error 404',
                              ),
                              style: FlutterFlowTheme.of(context)
                                  .headlineMedium
                                  .override(
                                    fontFamily: 'Outfit',
                                    letterSpacing: 0.0,
                                  ),
                            ),
                          ),
                          Padding(
                            padding: const EdgeInsetsDirectional.fromSTEB(
                                24.0, 4.0, 0.0, 0.0),
                            child: Text(
                              '€${getJsonField(
                                columnViewProdottoResponse.jsonBody,
                                r'''$.data.prezzo''',
                              ).toString()}',
                              style: FlutterFlowTheme.of(context)
                                  .headlineSmall
                                  .override(
                                    fontFamily: 'Outfit',
                                    letterSpacing: 0.0,
                                  ),
                            ),
                          ),
                          Padding(
                            padding: const EdgeInsetsDirectional.fromSTEB(
                                24.0, 16.0, 24.0, 0.0),
                            child: Text(
                              getJsonField(
                                columnViewProdottoResponse.jsonBody,
                                r'''$.data.descrizione''',
                              ).toString(),
                              style: FlutterFlowTheme.of(context)
                                  .labelMedium
                                  .override(
                                    fontFamily: 'Readex Pro',
                                    letterSpacing: 0.0,
                                  ),
                            ),
                          ),
                          Expanded(
                            child: Padding(
                              padding: const EdgeInsetsDirectional.fromSTEB(
                                  0.0, 0.0, 0.0, 24.0),
                              child: Column(
                                mainAxisSize: MainAxisSize.max,
                                mainAxisAlignment: MainAxisAlignment.end,
                                children: [
                                  Padding(
                                    padding: const EdgeInsetsDirectional.fromSTEB(
                                        32.0, 24.0, 32.0, 0.0),
                                    child: FFButtonWidget(
                                      onPressed: () async {
                                        _model.aggiungialcarrello =
                                            await AggiungiAlCarrelloCall.call(
                                          idCliente: FFAppState().idCliente,
                                          idOggetto: getJsonField(
                                            columnViewProdottoResponse.jsonBody,
                                            r'''$.data.id''',
                                          ),
                                        );
                                        if ((_model.aggiungialcarrello
                                                ?.succeeded ??
                                            true)) {
                                          context.pushNamed('Catalogo');
                                        } else {
                                          ScaffoldMessenger.of(context)
                                              .showSnackBar(
                                            SnackBar(
                                              content: Text(
                                                'Errore Sconosciuto',
                                                style: TextStyle(
                                                  color: FlutterFlowTheme.of(
                                                          context)
                                                      .primaryText,
                                                ),
                                              ),
                                              duration:
                                                  const Duration(milliseconds: 4000),
                                              backgroundColor:
                                                  FlutterFlowTheme.of(context)
                                                      .secondary,
                                            ),
                                          );
                                        }

                                        setState(() {});
                                      },
                                      text: 'Aggiungi al carrello',
                                      options: FFButtonOptions(
                                        width: double.infinity,
                                        height: 50.0,
                                        padding: const EdgeInsetsDirectional.fromSTEB(
                                            0.0, 0.0, 0.0, 0.0),
                                        iconPadding:
                                            const EdgeInsetsDirectional.fromSTEB(
                                                0.0, 0.0, 0.0, 0.0),
                                        color: FlutterFlowTheme.of(context)
                                            .primary,
                                        textStyle: FlutterFlowTheme.of(context)
                                            .titleSmall
                                            .override(
                                              fontFamily: 'Readex Pro',
                                              color: Colors.white,
                                              letterSpacing: 0.0,
                                            ),
                                        elevation: 3.0,
                                        borderSide: const BorderSide(
                                          color: Colors.transparent,
                                          width: 1.0,
                                        ),
                                      ),
                                    ),
                                  ),
                                ],
                              ),
                            ),
                          ),
                        ],
                      );
                    },
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
