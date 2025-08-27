#include <iostream>
#include <string>
#include <fstream>   // para manejar archivos
#include <cstdlib>   // para rand() y srand()
#include <ctime>     // para usar time() y crear valores aleatorios

using namespace std;

void generarCombinaciones(string alfabeto, int n, ofstream& archivo, string combinacionActual = "", int longitudActual = 0) {
    // Caso base: si la longitud de la combinacion actual es igual a n, la escribimos en el txt
    if (longitudActual == n) {
        archivo << combinacionActual << ",";
        return;
    }

    // Recorrer cada caracter del alfabeto y generar combinaciones
    for (char c : alfabeto) {
        generarCombinaciones(alfabeto, n, archivo, combinacionActual + c, longitudActual + 1);
    }
}
int main() {
    srand(time(0));  // Inicializar la semilla para números aleatorios

    string alfabeto = "01";
    int n;
    int opcion;

    do {
        cout << "Seleccione una opcion:\n";
        cout << "1. Ingresar el valor de n manualmente\n";
        cout << "2. Generar el valor de n aleatoriamente [1,1000]\n";
        cout << "3. Salir\n"; 
        cin >> opcion;

        if (opcion == 1) {
            cout << "Ingrese el valor de n: ";
            cin >> n;
        } else if (opcion == 2) {
            n = rand() % 1000 + 1;  // Generar un valor aleatorio entre 1 y 1000 para n
            cout << "Valor de n generado aleatoriamente: " << n << endl;
        } else if (opcion == 3) {
            cout << "Saliendo del programa.\n";
            return 0;
        } else {
            cout << "Opcion no valida. Por favor intente de nuevo.\n";
            continue;  // Volver al inicio del bucle
        }

        // Crear un archivo con el nombre que indica el valor de n
        string nombre_archivo = "combinaciones_n" + to_string(n) + ".txt";
        ofstream archivo(nombre_archivo);

        if (!archivo) {
            cout << "Error al crear el archivo.\n";
            return 1;
        }
        archivo << "ε,"; // Agregar la combinacion vacía al inicio del txt

        // Generar combinaciones por cada valor de n para formar el universo y escribirlas en el archivo
        for (int i = 1; i <= n; i++) {
            generarCombinaciones(alfabeto, i, archivo);
            //archivo << endl;  // Opcional: Separar las combinaciones por longitud con un salto de línea
        }

        archivo.close();
        cout << "Combinaciones generadas y guardadas en el archivo combinaciones_n" << n << ".txt\n";

        // Llamar al script de Python para graficar
        string comando = "python graficas.py " + nombre_archivo;
        system(comando.c_str());

    } while (opcion != 3); // Continuar hasta que el usuario elija salir

    return 0;
}
