#include <iostream>

using namespace std;

int main() {
    // Declaración del array de 10 elementos de tipo long int
    long int arr[10];

    // Ingresar los elementos del array
    cout << "Ingresa 10 numeros enteros tipo long int:\n";
    for(int i = 0; i < 10; i++) {
        cout << "Elemento " << i + 1 << ": ";
        cin >> arr[i];
    }

    // Mostrar la dirección de cada elemento del array
    cout << "\nDirección de cada elemento en el array:\n";
    for(int i = 0; i < 10; i++) {
        cout << "Dirección de arr[" << i << "] (" << arr[i] << ") : " << &arr[i] << endl;
    }

    // Realizar operaciones de suma y resta
    long int suma = 0, resta = arr[0]; // Inicializar resta con el primer elemento
    for(int i = 0; i < 10; i++) {
        suma += arr[i];
        if(i > 0) {
            resta -= arr[i];
        }
    }

    // Mostrar resultados y sus direcciones
    cout << "\nResultado de la suma: " << suma << " en la dirección: " << &suma << endl;
    cout << "Resultado de la resta: " << resta << " en la dirección: " << &resta << endl;

    return 0;
}