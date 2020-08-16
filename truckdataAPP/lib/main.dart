import './widgets/new_transactions.dart';

import './widgets/transaction_list.dart';

import 'dart:io';

import 'package:flutter/material.dart';
import './models/transactions.dart';
import './widgets/chart.dart';
import 'package:flutter/services.dart';
import 'package:flutter/cupertino.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Personal expenses',
      theme: ThemeData(
        primarySwatch: Colors.purple,
        accentColor: Colors.amber,
        errorColor: Colors.red[900],
        fontFamily: "Quicksand",
        textTheme: ThemeData.light().textTheme.copyWith(
              title: TextStyle(
                fontFamily: "OpenSans",
                fontSize: 18,
                fontWeight: FontWeight.bold,
              ),
              button: TextStyle(
                color: Colors.white,
              ),
            ),
        appBarTheme: AppBarTheme(
          textTheme: ThemeData.light().textTheme.copyWith(
                title: TextStyle(
                  fontFamily: "OpenSans",
                  fontSize: 20,
                  fontWeight: FontWeight.bold,
                ),
              ),
        ),
      ),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final List<Transcation> _userTrans = [];
  /* Transcation(
      id: 'a1',
      title: "Air pods pro",
      amount: 27500,
      date: DateTime.now(),
    ),
    Transcation(
      id: 'bq35',
      title: "Bose QC 35",
      amount: 29900,
      date: DateTime.now(),
    ),
  ]; */

  List<Transcation> get _recentTransaction {
    return _userTrans.where((element) {
      return element.date.isAfter(
        DateTime.now().subtract(
          Duration(
            days: 7,
          ),
        ),
      );
    }).toList();
  }

  void _addNewTransaction(
      String txtitle, double txamount, DateTime chosenDate) {
    final newTx = Transcation(
        id: DateTime.now().toString(),
        amount: txamount,
        date: chosenDate,
        title: txtitle);

    setState(() {
      _userTrans.add(newTx);
    });
  }

  void _deleteTransaction(String id) {
    setState(() {
      _userTrans.removeWhere((tx) {
        return tx.id == id;
      });
    });
  }

  void _startAddNewTransaction(BuildContext cxt) {
    showModalBottomSheet(
      context: cxt,
      builder: (_) {
        return NewTransaction(_addNewTransaction);
      },
    );
  }

  bool _showChart = false;

  @override
  Widget build(BuildContext context) {
    final mediaQuery = MediaQuery.of(context);
    final isLandScape = mediaQuery.orientation == Orientation.landscape;

    final PreferredSizeWidget appbar = Platform.isIOS
        ? CupertinoNavigationBar(
            middle: Text(
              "Personal Expenses",
            ),
            trailing: Row(
              mainAxisSize: MainAxisSize.min,
              children: <Widget>[
                GestureDetector(
                  onTap: () => _startAddNewTransaction(context),
                  child: Icon(CupertinoIcons.add),
                ),
              ],
            ),
          )
        : AppBar(
            title: Text('Personal Expenses'),
            actions: <Widget>[
              IconButton(
                icon: Icon(Icons.add),
                onPressed: () => _startAddNewTransaction(context),
              )
            ],
          );

    final _pageBody = SafeArea(
      child: SingleChildScrollView(
        child: Column(
          //mainAxisAlignment: MainAxisAlignment.spaceAround,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: <Widget>[
            if (isLandScape)
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  Text(
                    "Show Chart",
                    style: Theme.of(context).textTheme.title,
                  ),
                  Switch.adaptive(
                    value: _showChart,
                    onChanged: (val) {
                      setState(() {
                        _showChart = val;
                      });
                    },
                  )
                ],
              ),
            if (isLandScape)
              _showChart
                  ? Container(
                      child: Chart(_recentTransaction),
                      height: (mediaQuery.size.height -
                              appbar.preferredSize.height -
                              mediaQuery.padding.top) *
                          0.65,
                    )
                  : Container(
                      child: TransactionList(_userTrans, _deleteTransaction),
                      height: (mediaQuery.size.height -
                              appbar.preferredSize.height -
                              mediaQuery.padding.top) *
                          0.75,
                    ),
            if (!isLandScape)
              Container(
                child: Chart(_recentTransaction),
                height: (mediaQuery.size.height -
                        appbar.preferredSize.height -
                        mediaQuery.padding.top) *
                    0.25,
              ),
            if (!isLandScape)
              Container(
                child: TransactionList(_userTrans, _deleteTransaction),
                height: (mediaQuery.size.height -
                        appbar.preferredSize.height -
                        mediaQuery.padding.top) *
                    0.75,
              ),
          ],
        ),
      ),
    );

    return Platform.isIOS
        ? CupertinoPageScaffold(
            child: _pageBody,
            navigationBar: appbar,
          )
        : Scaffold(
            appBar: appbar,
            body: _pageBody,
            floatingActionButtonLocation:
                FloatingActionButtonLocation.centerFloat,
            floatingActionButton: Platform.isIOS
                ? Container()
                : FloatingActionButton(
                    child: Icon(Icons.add),
                    onPressed: () => _startAddNewTransaction(context),
                  ),
          );
  }
}
