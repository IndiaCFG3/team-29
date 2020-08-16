import 'package:flutter/foundation.dart';

class Transcation {
  final String id;
  final String title;
  final double amount;
  DateTime date;

  Transcation({
    @required this.id,
    @required this.amount,
    @required this.date,
    @required this.title,
  });
}
