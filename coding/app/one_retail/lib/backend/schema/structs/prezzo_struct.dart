// ignore_for_file: unnecessary_getters_setters

import '/backend/schema/util/schema_util.dart';

import 'index.dart';
import '/flutter_flow/flutter_flow_util.dart';

class PrezzoStruct extends BaseStruct {
  PrezzoStruct({
    List<double>? prezzo,
  }) : _prezzo = prezzo;

  // "prezzo" field.
  List<double>? _prezzo;
  List<double> get prezzo => _prezzo ?? const [];
  set prezzo(List<double>? val) => _prezzo = val;
  void updatePrezzo(Function(List<double>) updateFn) =>
      updateFn(_prezzo ??= []);
  bool hasPrezzo() => _prezzo != null;

  static PrezzoStruct fromMap(Map<String, dynamic> data) => PrezzoStruct(
        prezzo: getDataList(data['prezzo']),
      );

  static PrezzoStruct? maybeFromMap(dynamic data) =>
      data is Map ? PrezzoStruct.fromMap(data.cast<String, dynamic>()) : null;

  Map<String, dynamic> toMap() => {
        'prezzo': _prezzo,
      }.withoutNulls;

  @override
  Map<String, dynamic> toSerializableMap() => {
        'prezzo': serializeParam(
          _prezzo,
          ParamType.double,
          true,
        ),
      }.withoutNulls;

  static PrezzoStruct fromSerializableMap(Map<String, dynamic> data) =>
      PrezzoStruct(
        prezzo: deserializeParam<double>(
          data['prezzo'],
          ParamType.double,
          true,
        ),
      );

  @override
  String toString() => 'PrezzoStruct(${toMap()})';

  @override
  bool operator ==(Object other) {
    const listEquality = ListEquality();
    return other is PrezzoStruct && listEquality.equals(prezzo, other.prezzo);
  }

  @override
  int get hashCode => const ListEquality().hash([prezzo]);
}

PrezzoStruct createPrezzoStruct() => PrezzoStruct();
