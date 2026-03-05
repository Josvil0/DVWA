# 🛡️ Auditoría de Seguridad: DVWA

**Autor:** Jose Alonso Villanova

---

## 1. Introducción
El presente informe detalla las pruebas de penetración realizadas sobre la plataforma DVWA (Damn Vulnerable Web Application) desplegada en un contenedor Docker. Se analizan vectores de ataque como Inyección de Comandos, File Upload y Brute Force, evaluando cómo las configuraciones de seguridad afectan la viabilidad de los exploits.

---

## 🎯 Objetivos
* Identificar y explotar vulnerabilidades web comunes (OWASP Top 10).
* Analizar los mecanismos de defensa en diferentes niveles de seguridad (Low/Medium).
* Documentar los vectores de ataque y las técnicas de remediación.

---

## 📁 Índice de Prácticas

Haz clic en cada sección para acceder al detalle técnico de la vulnerabilidad:

1. [**Ataque de Fuerza Bruta (Brute Force)**](./1.Ataque%20de%20fuerza%20Bruta/)
2. [**Inyección de Comandos (Command Injection)**](./2.Inyeccion%20de%20comandos/)
3. [**Cross-Site Request Forgery (CSRF)**](./3.Cross-Site%20Request%20Forgery%20(CSRF)/)
4. [**File Inclusion**](./4.File%20Inclusion/)
5. [**File Upload: Obtención de Shell Inversa**](./5.File%20Upload%20:%20Shell%20inversa/)
6. [**Inyección SQL (SQL Injection)**](./6.Inyeccion%20SQL/)
7. [**Blind SQL Injection**](./7.Blind%20SQL%20injection/)
8. [**IDs de Sesión Débiles**](./8.IDs%20de%20sesion%20debiles/)
9. [**DOM Based Cross Site Scripting (XSS)**](./9.DOM%20Based%20Cross%20Site%20Scripting%20(XSS)/)
10. [**Reflected Cross Site Scripting (XSS)**](./10.Reflected%20Cross%20Site%20Scripting%20(XSS)/)
11. [**Stored Cross site Scripting**](./11.Stored%20Cross%20site%20Scripting/)
12. [**Content Security Policy (CSP) Bypass**](./12.Content%20Security%20Policy%20(CSP)%20Bypass/)
13. [**JavaScript Attacks**](./13.JavaScript%20Attacks/)

---

## 3. Conclusiones Generales
La principal lección de este laboratorio es que no se puede confiar en el usuario. En una puesta en producción segura, la clave no es solo limpiar lo que nos envían, sino usar herramientas que separen los datos de las órdenes, como las consultas preparadas, para que el servidor nunca confunda una contraseña con un comando dañino.

---
© 2026 Jose Alonso Villanova - Publicado bajo Licencia CC BY-SA 4.0
