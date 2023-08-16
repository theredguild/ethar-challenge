# Challenge de Ethereum Argentina

![banner](./assets/banner.png)

Jugá este challenge y participá del sorteo de un hardware wallet!

## Contexto y objetivo

Hay un contrato que se llama `MultiSig` que permite ejecutar operaciones.

Para ejecutarlas, se requieren las firmas de los operadores autorizados del contrato.

El objetivo es que logres ejecutar una operación como **uno solo** de los firmantes del autorizados, **sin necesidad de las otras firmas**.

## Sorteo

Cuando juegues el desafío vas a generar un ticket único que te permitirá ser parte del sorteo. Anotá el número de ticket, y ya estarás participando!

Los ganadores serán anunciados al final de la conferencia.

## Requisitos

- [Foundry](https://book.getfoundry.sh/), para la ejecución del challenge.
- [Python](https://www.python.org/downloads/), para el uso de llaves privadas de prueba.

## Setup

1. Cloná este repositorio

```
git clone https://github.com/ethereum-argentina/coding-challenge
```

2. Instalá las dependencias

```
pip install -r requirements.txt
```

3. Probá que todo funcione bien 

```
forge test
```

4. Mirá y guardá tu número único de ticket para el sorteo! Lo vas a encontrar en el archivo generado en el directorio raiz del desafío.

5. Encontrá la falla del contrato `MultiSig`, y modificá el archivo de test `MultiSig.t.sol` de tal forma que cumplas con el objetivo. Vas a necesitar mostrar la solución para que te otorguemos el premio si tu número de ticket es el ganador del sorteo.


SPAWNED#############################################################################################