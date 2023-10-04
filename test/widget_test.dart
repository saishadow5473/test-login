import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:samplemobile/main.dart';

void main() {
  testWidgets('Login page UI test', (WidgetTester tester) async {
    // Build our app and trigger a frame.
    await tester.pumpWidget(const MyApp());

    // Verify that the title is correct.
    expect(find.text('Login App'), findsOneWidget);

    // Enter a valid email and password
    await tester.enterText(find.byType(TextFormField).at(0), 'arun@gogosoon.com');
    await tester.enterText(find.byType(TextFormField).at(1), 'qazxswedcvfr');

    // Tap the login button.
    await tester.tap(find.byType(ElevatedButton));
    // Wait for animations or async operations to complete.
    await tester.pumpAndSettle();

    // Verify that we are on the home page.
    expect(find.text('Home Page'), findsOneWidget);
    expect(find.text('arun@gogosoon.com'), findsOneWidget);

    // Tap the "Go back!" button.
    await tester.tap(find.byType(ElevatedButton));
    // Wait for animations or async operations to complete.
    await tester.pumpAndSettle();

    // Verify that we are back on the login page.
    expect(find.text('Login App'), findsOneWidget);
  });
}
