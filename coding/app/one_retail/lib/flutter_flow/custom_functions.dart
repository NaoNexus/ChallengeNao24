import 'dart:convert';
import 'dart:math' as math;

import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:intl/intl.dart';
import 'package:timeago/timeago.dart' as timeago;
import 'lat_lng.dart';
import 'place.dart';
import 'uploaded_file.dart';

String? uRLmerge(
  String? staticstring,
  String? urlstring,
) {
  // merge two strings, but remove the first two characters from the second one
  if (staticstring == null || urlstring == null) {
    return null;
  }
  if (urlstring.length < 2) {
    return staticstring + urlstring;
  }
  return staticstring + urlstring.substring(2);
}

String? capitalize(String? input) {
  // a function that capitalizes the first letter of every word of a string
  if (input == null) {
    return null;
  }
  return input.split(' ').map((word) {
    if (word.isEmpty) {
      return word;
    }
    return word[0].toUpperCase() + word.substring(1);
  }).join(' ');
}

double? totalPrice(List<double>? prodotti) {
  // calculate total sum of list items
  if (prodotti == null || prodotti.isEmpty) {
    return null;
  }
  double sum = 0.0;
  for (double prodotto in prodotti) {
    sum += prodotto;
  }
  return sum;
}
