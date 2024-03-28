import 'dart:convert';

import 'api_manager.dart';

export 'api_manager.dart' show ApiCallResponse;

const _kPrivateApiFunctionName = 'ffPrivateApiCall';

class LoginCall {
  static Future<ApiCallResponse> call({
    String? username = 'giovanni_bellorio',
    String? password = 'gb',
  }) async {
    final ffApiRequestBody = '''
{
  "username": "$username",
  "password": "$password"
}''';
    return ApiManager.instance.makeApiCall(
      callName: 'login',
      apiUrl:
          'http://192.168.0.170:5010/api/utente/app/%7B\'username\':%20\'$username\',%20\'password\':%20\'$password\'%7D',
      callType: ApiCallType.POST,
      headers: {},
      params: {},
      body: ffApiRequestBody,
      bodyType: BodyType.JSON,
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      alwaysAllowBody: false,
    );
  }
}

class ViewCarrelloCall {
  static Future<ApiCallResponse> call({
    int? idCliente,
    String? nome = '',
    String? cognome = '',
  }) async {
    return ApiManager.instance.makeApiCall(
      callName: 'view carrello',
      apiUrl:
          'http://192.168.0.170:5010/api/carrello/%7B\'cognome\':%20\'$cognome\',%20\'id_cliente\':%20$idCliente,%20\'nome\':%20\'$nome\'%7D',
      callType: ApiCallType.GET,
      headers: {},
      params: {},
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      alwaysAllowBody: false,
    );
  }
}

class ViewCatalogoCall {
  static Future<ApiCallResponse> call() async {
    return ApiManager.instance.makeApiCall(
      callName: 'view catalogo',
      apiUrl: 'http://192.168.0.170:5010/api/catalogo',
      callType: ApiCallType.GET,
      headers: {},
      params: {},
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      alwaysAllowBody: false,
    );
  }
}

class ViewProdottoCall {
  static Future<ApiCallResponse> call({
    int? id = 1,
  }) async {
    return ApiManager.instance.makeApiCall(
      callName: 'view prodotto',
      apiUrl: 'http://192.168.0.170:5010/api/prodotto/$id',
      callType: ApiCallType.GET,
      headers: {},
      params: {},
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      alwaysAllowBody: false,
    );
  }
}

class ViewProdottoQrCall {
  static Future<ApiCallResponse> call({
    String? qr = '',
  }) async {
    return ApiManager.instance.makeApiCall(
      callName: 'view prodotto qr',
      apiUrl: '$qr',
      callType: ApiCallType.GET,
      headers: {},
      params: {},
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      alwaysAllowBody: false,
    );
  }
}

class AggiungiAlCarrelloCall {
  static Future<ApiCallResponse> call({
    int? idCliente,
    int? idOggetto,
  }) async {
    final ffApiRequestBody = '''
{
  "id_cliente": $idCliente,
  "id_oggetto": $idOggetto
}''';
    return ApiManager.instance.makeApiCall(
      callName: 'aggiungi al carrello',
      apiUrl:
          'http://192.168.0.170:5010/api/carrello/%7B\'id_cliente\':%2$idCliente,%20\'id_oggetto\':%20$idOggetto%7D',
      callType: ApiCallType.POST,
      headers: {},
      params: {},
      body: ffApiRequestBody,
      bodyType: BodyType.JSON,
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      alwaysAllowBody: false,
    );
  }
}

class IniziaDialogoCall {
  static Future<ApiCallResponse> call({
    String? nome = '',
    String? cognome = '',
    int? idCliente,
  }) async {
    final ffApiRequestBody = '''
{
  "id_cliente": $idCliente,
  "nome": "$nome",
  "cognome": "$cognome"
}''';
    return ApiManager.instance.makeApiCall(
      callName: 'inizia dialogo',
      apiUrl:
          'http://192.168.0.170:5010/api/utente/dialogo/%7B\'cognome\':%20\'$cognome\',%20\'id_cliente\':%20$idCliente,%20\'nome\':%20\'$nome\'%7',
      callType: ApiCallType.POST,
      headers: {},
      params: {},
      body: ffApiRequestBody,
      bodyType: BodyType.JSON,
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      alwaysAllowBody: false,
    );
  }
}

class RimuoviDalCarrelloCall {
  static Future<ApiCallResponse> call({
    int? idCliente,
    int? idOggetto,
  }) async {
    return ApiManager.instance.makeApiCall(
      callName: 'rimuovi dal carrello',
      apiUrl:
          'http://192.168.0.170:5010/api/carrello/%7B\'id_oggetto\':%20$idOggetto,%20\'id_cliente\':%20$idCliente%7D',
      callType: ApiCallType.DELETE,
      headers: {},
      params: {},
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      alwaysAllowBody: false,
    );
  }
}

class ConfermaOrdineCall {
  static Future<ApiCallResponse> call({
    int? idCliente,
  }) async {
    final ffApiRequestBody = '''
{
  "id_cliente": $idCliente,
  "modalita_pagamento": "carta"
}''';
    return ApiManager.instance.makeApiCall(
      callName: 'conferma ordine',
      apiUrl:
          'http://192.168.0.170:5010/api/ordine/%7B\'id_cliente\':%20$idCliente,%20\'modalita_pagamento\':%20\'carta\'%7D',
      callType: ApiCallType.POST,
      headers: {},
      params: {},
      body: ffApiRequestBody,
      bodyType: BodyType.JSON,
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      alwaysAllowBody: false,
    );
  }
}

class DescrizioneNAOCall {
  static Future<ApiCallResponse> call({
    int? idOggetto,
  }) async {
    return ApiManager.instance.makeApiCall(
      callName: 'Descrizione NAO',
      apiUrl: 'http://192.168.0.170:5010/api/descrizione_prodotto/$idOggetto',
      callType: ApiCallType.GET,
      headers: {},
      params: {},
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      alwaysAllowBody: false,
    );
  }
}

class OrdineMobileCall {
  static Future<ApiCallResponse> call({
    int? idCliente,
  }) async {
    return ApiManager.instance.makeApiCall(
      callName: 'ordine mobile',
      apiUrl:
          'http://192.168.0.170:5010/api/ordine_mobile/%7B\'id_cliente\':%20$idCliente,%20\'modalita_pagamento\':%20\'carta\'%7D',
      callType: ApiCallType.POST,
      headers: {},
      params: {},
      bodyType: BodyType.JSON,
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      alwaysAllowBody: false,
    );
  }
}

class ApiPagingParams {
  int nextPageNumber = 0;
  int numItems = 0;
  dynamic lastResponse;

  ApiPagingParams({
    required this.nextPageNumber,
    required this.numItems,
    required this.lastResponse,
  });

  @override
  String toString() =>
      'PagingParams(nextPageNumber: $nextPageNumber, numItems: $numItems, lastResponse: $lastResponse,)';
}

String _serializeList(List? list) {
  list ??= <String>[];
  try {
    return json.encode(list);
  } catch (_) {
    return '[]';
  }
}

String _serializeJson(dynamic jsonVar, [bool isList = false]) {
  jsonVar ??= (isList ? [] : {});
  try {
    return json.encode(jsonVar);
  } catch (_) {
    return isList ? '[]' : '{}';
  }
}
