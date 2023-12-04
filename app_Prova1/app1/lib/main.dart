import 'package:flutter/material.dart';
import 'package:camera/camera.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  // Ottieni la lista delle telecamere disponibili
  final cameras = await availableCameras();
  // Scegli la prima telecamera disponibile
  final firstCamera = cameras.first;

  runApp(MyApp(camera: firstCamera));
}

class MyApp extends StatelessWidget {
  final CameraDescription camera;

  const MyApp({Key? key, required this.camera}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Naonexus', camera: camera),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title, required this.camera})
      : super(key: key);

  final String title;
  final CameraDescription camera;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  Future<void> _openCamera() async {
    // Quando il pulsante viene premuto, naviga alla pagina della fotocamera
    await Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => CameraPage(camera: widget.camera),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              widget.title,
              style: TextStyle(fontSize: 24),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: _openCamera,
              child: Text('Apri Fotocamera'),
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {},
        tooltip: 'Increment',
        child: const Icon(Icons.add),
      ),
    );
  }
}

class CameraPage extends StatefulWidget {
  final CameraDescription camera;

  const CameraPage({Key? key, required this.camera}) : super(key: key);

  @override
  _CameraPageState createState() => _CameraPageState();
}

class _CameraPageState extends State<CameraPage> {
  late CameraController _controller;
  late Future<void> _initializeControllerFuture;

  @override
  void initState() {
    super.initState();
    // Crea un controller per la telecamera
    _controller = CameraController(
      widget.camera,
      ResolutionPreset.medium,
    );
    // Inizializza il controller. Questo è necessario prima di utilizzare la telecamera.
    _initializeControllerFuture = _controller.initialize();
  }

  @override
  void dispose() {
    // Rilascia il controller quando l'app viene chiusa
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Fotocamera'),
      ),
      // Attendere fino a quando il controller non è inizializzato prima di visualizzare la telecamera
      body: FutureBuilder(
        future: _initializeControllerFuture,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.done) {
            // Se il controller è inizializzato, mostra la vista della telecamera
            return CameraPreview(_controller);
          } else {
            // Altrimenti, mostra un indicatore di caricamento
            return Center(child: CircularProgressIndicator());
          }
        },
      ),
    );
  }
}