# [1.0.0](https://github.com/ZR-TECDI/zrstats/compare/v0.2.0...v1.0.0) (2019-11-18)


### Bug Fixes

* **asistencia:** funcionando otra vez el script de asistencia ([3873219](https://github.com/ZR-TECDI/zrstats/commit/3873219e45e87dd3983d6957aa473978b3eb973f))
* **builder:** anda llorando porque no hay ssh keys ([51cddb1](https://github.com/ZR-TECDI/zrstats/commit/51cddb1dc0536c1402208ff7b667e0b8618eb403))
* **migration:** hacer manage.py migrate ([16a5bb2](https://github.com/ZR-TECDI/zrstats/commit/16a5bb2bb66d1011eb97b5e6c0999af2859a8c90))
* **migrations:** agrego migraciones. Dentro de poco habria resetearlas. ([558f41d](https://github.com/ZR-TECDI/zrstats/commit/558f41ddf8c7c79b3b9ddc5deff5e6a1a51865a5))
* **models:** datos_iniciales ahora fabrica miembros exitosamente ([9bf0e40](https://github.com/ZR-TECDI/zrstats/commit/9bf0e40f5cde206b9e0ec2afb5f554dc3e112819))
* **models:** long. nombre de pais aumentada a 40, abrev. reducida a 2 ([7f60229](https://github.com/ZR-TECDI/zrstats/commit/7f60229cf7cf010753e94e59a65c30252e99da50))
* **procesar_rpt:** fix cuando no tiene hora de desconexion ([1b64de6](https://github.com/ZR-TECDI/zrstats/commit/1b64de620ccf80e8d878f8bd4b01d99d661f3f68))
* **procesar_rpt:** fixes varios, ahora crea y asgina campaña a la mision ([ab05721](https://github.com/ZR-TECDI/zrstats/commit/ab057210f54bed410a90a9c0ac8c49b9ce0b37b5))
* **repo:** agregado uploads al .gitignore ([3b51f7a](https://github.com/ZR-TECDI/zrstats/commit/3b51f7a50903a6b292a5bb87db031e07facb9249))
* **reporte:** corrijo la asignacion de campo 'autor' del reporte ([3a083a9](https://github.com/ZR-TECDI/zrstats/commit/3a083a969438e57e0b39f230c6cc017543123837))
* **subir_reporte:** procesa los datos de misión del reporte ([422f9e7](https://github.com/ZR-TECDI/zrstats/commit/422f9e7595dcd8408b5cb4c9a8cf75c632c9cd77))
* **template:** corregidos CRUDs de Miembro ([3e75fc1](https://github.com/ZR-TECDI/zrstats/commit/3e75fc13832748afa3290704670b2b8d8913266b))
* **template:** corregidos CRUDs de Miembro parte2 ([3eb0836](https://github.com/ZR-TECDI/zrstats/commit/3eb0836bc7217d717f4cc7a069f0ba6e87207b1f))


### Code Refactoring

* **settings:** secretos como variables de entorno ([7b279e1](https://github.com/ZR-TECDI/zrstats/commit/7b279e1a46e0a1b1f46765f02fa8977030e81e86))
* **template:** corregidos templates de crud y agregado crispy form ([5edbd02](https://github.com/ZR-TECDI/zrstats/commit/5edbd0210898602df1e1993bafdc854c6b2491fc))


### Features

* **calendar:** view, template y url de fullcalendar de misiones ([19b299a](https://github.com/ZR-TECDI/zrstats/commit/19b299a1f3fc24b973cb3ffa34ce73db0bc7c476))
* **comandos:** removido el llamado de datos_iniciales en wsgi.py ([a455cef](https://github.com/ZR-TECDI/zrstats/commit/a455cef5d5428d8704d47bf5f06d41649e8a858e))
* **CRUDs:** models, views, urls y templates para todos los CRUDs ([81b5dac](https://github.com/ZR-TECDI/zrstats/commit/81b5dac92c1d49a729cd7125fcfe4366177a42a0))
* **datatables:** subo a static modulo dataTables para renderizar tablas ([36e02dc](https://github.com/ZR-TECDI/zrstats/commit/36e02dcd91afa39528e36edf81516eec91a7b224))
* **datos_iniciales:** agrego un superuser admin al datos_iniciales ([21feeda](https://github.com/ZR-TECDI/zrstats/commit/21feedab5565f5c6b0c8cbcebb3c8fcd4599274b))
* **datos_iniciales:** genera 1 año de campañas, misiones y asistencias ([589b950](https://github.com/ZR-TECDI/zrstats/commit/589b95050621c4a6de8270ee7f5816a3d9338100))
* **datos_iniciales:** todos los paises del mundo (ISO 3166 alfa 2) ([150007d](https://github.com/ZR-TECDI/zrstats/commit/150007daddbec8393e60fb349f7fb9797f43d97e))
* **login:** agregado sistema de cambiar contraseña ([7768568](https://github.com/ZR-TECDI/zrstats/commit/7768568be325f8f038faa55c58050784d252ac7e))
* **login:** implementada página de login ([94f810b](https://github.com/ZR-TECDI/zrstats/commit/94f810b6249d464a0154dbe5136fb345bec6a2b9))
* **models:** Agregado en wsgi.py el llamado a datos_iniciales.py ([f5b8180](https://github.com/ZR-TECDI/zrstats/commit/f5b8180b80a4fb7b447597e62c002be5fb25e78c))
* **models:** agrego nuevos campos a Mision, correr nuevas migrations ([884b7ad](https://github.com/ZR-TECDI/zrstats/commit/884b7adc4060d24855a57c238a595ff1b778b6f4))
* **models:** nuevo modelo Campaña ([f53cbac](https://github.com/ZR-TECDI/zrstats/commit/f53cbac700d75d8a187ce29910db9ea2faa39d7b))
* **models:** wip script de datos iniciales [skip ci] ([bb7a1ab](https://github.com/ZR-TECDI/zrstats/commit/bb7a1abdccd20531c21a62b551b7262ba42da95b))
* **pipeline:** sistema de build para el live server ([6b62f36](https://github.com/ZR-TECDI/zrstats/commit/6b62f3649e4d0e3690e0af443699d2a96a86de13))
* **procesar_reporte:** comprobación de rangos y licencia/reserva ([52dd7ab](https://github.com/ZR-TECDI/zrstats/commit/52dd7aba5bb7217cb993ccb4eb52866580ea9fb3))
* **signup:** formulario de signup y proceso para reiniciar contraseña ([ab55ccc](https://github.com/ZR-TECDI/zrstats/commit/ab55cccc1361b372bb1d525acd2cbb1f8f19572a))
* **subir_reporte:** form basico para generar mision con solo el reporte ([d568dcb](https://github.com/ZR-TECDI/zrstats/commit/d568dcbd6cb127ebf0f41c4f0f604dda986127d4))
* **template:** agrego select2 a los formularios para campos M2M ([01bea74](https://github.com/ZR-TECDI/zrstats/commit/01bea748f705cdd764516b79db623501c32b5d9b))
* **template:** ATENCIÓN, pip install django-bootstrap-datepicker-plus ([1d9fe24](https://github.com/ZR-TECDI/zrstats/commit/1d9fe241f1d5310b40525be996ec96f40ee7641a))
* **template:** creado un perfil mockup ([bd9af7e](https://github.com/ZR-TECDI/zrstats/commit/bd9af7ead1c20c0eca0fa411471308f2fefb2388))
* **template:** filtrado por tipo de mision en Mision List ([cfcf68f](https://github.com/ZR-TECDI/zrstats/commit/cfcf68fcdcc69e16c39de1782c274b1c885ebc10))
* **template:** filtros en tablas ([919bf29](https://github.com/ZR-TECDI/zrstats/commit/919bf2966259c172598219f310a9034c674ee07f))
* **template:** formularios, URLs y views de los CRUD para Campaña ([add8774](https://github.com/ZR-TECDI/zrstats/commit/add87743cdc93198d3b53a99b7f1e6152f8ef191))
* **template:** funcion de borrar misiones (y asistencia relacionada) ([8100c64](https://github.com/ZR-TECDI/zrstats/commit/8100c64d4a54446adfddc29cb52bfd1370fbb219))
* **template:** listado de misiones mas pro ([59b14ef](https://github.com/ZR-TECDI/zrstats/commit/59b14efdddba5c76533b54388061ad6f2078895d))
* **template:** subido un paquete css con las banderas del mundo ([2e3a404](https://github.com/ZR-TECDI/zrstats/commit/2e3a4047dc67986b6fc4307ad94b81d938201337))
* **test_page:** agrego una view+template+url para testing ([e99b721](https://github.com/ZR-TECDI/zrstats/commit/e99b7214eb74af6776231b5e8050ab4659cebb96))
* **view:** agregada vista para ver la asistencia de un mes ([c69deaa](https://github.com/ZR-TECDI/zrstats/commit/c69deaaa5e9e709a289e66dbf03ae1f71e07bf86))


### BREAKING CHANGES

* **settings:** Hay que setear correctarmente las variables de entorno a partir de ahora
* **template:** hacer pip install django_select2
* **template:** instalar django-crispy-forms y django-extensions

# [0.2.0](https://github.com/ZR-TECDI/zrstats/compare/v0.1.0...v0.2.0) (2019-09-13)


### Bug Fixes

* **migrations:** reparado el cagazo (quizás) ([f98cc21](https://github.com/ZR-TECDI/zrstats/commit/f98cc21))
* **tests:** corregida configuración de travis ([33b0688](https://github.com/ZR-TECDI/zrstats/commit/33b0688))
* **tests:** corregido script de tests en travis ([cf3ed84](https://github.com/ZR-TECDI/zrstats/commit/cf3ed84))


### Features

* **tests:** WIP agregados archivos de tests ([324b52a](https://github.com/ZR-TECDI/zrstats/commit/324b52a))

# 0.1.0 (2019-09-13)


### Bug Fixes

* **pipeline:** se me olvidó el . en los nombres :monkey: ([374cd0d](https://github.com/ZR-TECDI/zrstats/commit/374cd0d))


### Features

* **pipeline:** agregada conf de semantic-release ([4c70bdb](https://github.com/ZR-TECDI/zrstats/commit/4c70bdb))
* **pipeline:** agregada configuración inicial de Travis ([7616638](https://github.com/ZR-TECDI/zrstats/commit/7616638))
* **pipeline:** agregada configuración mergify ([44f05c0](https://github.com/ZR-TECDI/zrstats/commit/44f05c0))
