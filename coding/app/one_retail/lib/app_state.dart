import 'package:flutter/material.dart';

class FFAppState extends ChangeNotifier {
  static FFAppState _instance = FFAppState._internal();

  factory FFAppState() {
    return _instance;
  }

  FFAppState._internal();

  static void reset() {
    _instance = FFAppState._internal();
  }

  Future initializePersistedState() async {}

  void update(VoidCallback callback) {
    callback();
    notifyListeners();
  }

  int _idCliente = 0;
  int get idCliente => _idCliente;
  set idCliente(int value) {
    _idCliente = value;
  }

  String _nome = '';
  String get nome => _nome;
  set nome(String value) {
    _nome = value;
  }

  String _cognome = '';
  String get cognome => _cognome;
  set cognome(String value) {
    _cognome = value;
  }

  bool _ordineMobile = false;
  bool get ordineMobile => _ordineMobile;
  set ordineMobile(bool value) {
    _ordineMobile = value;
  }
}
