# Tema minimalista por horario para Samsung Galaxy A55

Cuatro fondos minimalistas (1080x2340) y la receta para cambiarlos por franja
horaria **sin root**.

Los fondos se regeneran con `python3 generate_wallpapers.py` (requiere Pillow).

| Modo | Horario | Fondo | Ajustes |
|---|---|---|---|
| Conducción | 07:00–09:00 | `wallpapers/conduccion.png` | Modo oscuro, mapas, Bluetooth |
| Trabajo | 09:00–17:00 | `wallpapers/trabajo.png` | Modo claro, No molestar con excepciones |
| Familia | 17:00–23:00 | `wallpapers/familia.png` | Modo claro, notificaciones normales |
| Relax | 23:00–06:59 | `wallpapers/relax.png` | Modo oscuro, brillo bajo, luz azul |

Los horarios de Trabajo (9–17) y de Relax (23–6:59) son supuestos. Cámbialos
en los perfiles si los tuyos son distintos.

## Qué falta (no se puede hacer desde este repositorio)

Este repositorio no puede instalar nada en el teléfono, y los perfiles de Tasker
**no están incluidos ni probados**: hay que crearlos en el teléfono.

1. Copia la carpeta `wallpapers/` al teléfono (por ejemplo a `Pictures/Temas`).
2. Instala los APK solo desde sus repositorios oficiales: Tasker o MacroDroid y,
   si quieres un launcher austero, Olauncher.
3. Concede a Tasker el permiso de ajustes seguros (una sola vez, con ADB desde
   un PC o con Shizuku; no hace falta root):

   ```
   adb shell pm grant net.dinglisch.android.taskerm android.permission.WRITE_SECURE_SETTINGS
   ```

4. En Tasker crea 4 perfiles con la condición **Hora** de la tabla. Cada uno
   lanza una tarea con estas acciones:
   - Pantalla → **Fondo de pantalla** (la imagen del modo).
   - Pantalla → **Brillo** (bajo en Relax, automático en el resto).
   - Sistema → **Modo oscuro** (según la tabla).
   - Opcional: abrir la app de mapas en Conducción.
5. Deja a **Modos y rutinas** de Samsung solo lo suyo: No molestar, sonidos y
   notificaciones.

## Probar

Ejecuta cada tarea a mano desde Tasker y comprueba que cambian el fondo y el
modo oscuro. Después deja los perfiles activos.
