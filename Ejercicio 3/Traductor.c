// Traductor.c
// Programa para traducir palabras reservadas de C a español.

#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Estructura para el diccionario de traducción
typedef struct {
  char *ingles;
  char *espanol;
} Diccionario;

Diccionario traducciones[] = {
    {"int", "entero"},      {"float", "flotante"},  {"char", "caracter"},
    {"if", "si"},           {"else", "sino"},       {"while", "mientras"},
    {"for", "para"},        {"return", "retornar"}, {"void", "vacio"},
    {"switch", "segun"},    {"case", "caso"},       {"break", "romper"},
    {"default", "defecto"}, {"do", "hacer"},        {"struct", "estructura"}};

#define TOTAL_KEYWORDS (sizeof(traducciones) / sizeof(Diccionario))

// Función para buscar la traducción de una palabra
const char *traducir(char *palabra) {
  for (int i = 0; i < TOTAL_KEYWORDS; i++) {
    if (strcmp(palabra, traducciones[i].ingles) == 0) {
      return traducciones[i].espanol;
    }
  }
  return palabra; // Si no es reservada, devuelve la original
}

int main() {
  // 1. Uso de memoria dinámica para cargar el código
  size_t capacidad = 1024;
  char *codigo = (char *)malloc(capacidad * sizeof(char));

  if (codigo == NULL) {
    printf("Error: No se pudo asignar memoria.\n");
    return 1;
  }

  printf("Ingresa una linea de codigo en C (ej: int x = 10; if (x > 5) return "
         "0;):\n");
  fgets(codigo, capacidad, stdin);

  printf("\n--- CODIGO TRADUCIDO ---\n");

  // 2. Tokenización y procesamiento
  char *delimitadores = " \t\n(),;{}";
  char *copia_codigo =
      strdup(codigo); // Copia para no destruir el original con strtok
  char *token = strtok(copia_codigo, delimitadores);

  // El problema de strtok es que pierde los delimitadores.
  // Para una traducción simple de "palabras encontradas", lo imprimiremos
  // secuencialmente:

  char *p = codigo;
  char palabra[50];
  int idx = 0;

  while (*p != '\0') {
    if (isalpha(*p)) {
      palabra[idx++] = *p;
    } else {
      if (idx > 0) {
        palabra[idx] = '\0';
        printf("%s", traducir(palabra));
        idx = 0;
      }
      printf("%c", *p);
    }
    p++;
  }

  // 3. Liberar memoria dinámica
  free(codigo);
  free(copia_codigo);

  return 0;
}