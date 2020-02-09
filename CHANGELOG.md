# [1.1.0](https://github.com/ZR-TECDI/zrstats/compare/v1.0.0...v1.1.0) (2020-02-09)


### Bug Fixes

* **calendario:** el alto del div se ajusta al contenido del calendario ([b00efea](https://github.com/ZR-TECDI/zrstats/commit/b00efeac59fc82f440df958f61596aa7ef079615))
* **commands:** correcion en el comando datos_iniciales ([36277ac](https://github.com/ZR-TECDI/zrstats/commit/36277aca26974035c050fc1a008dc84931ecee16))
* **datatables:** corrijo datatables en todos los templates con tabla ([7ee0469](https://github.com/ZR-TECDI/zrstats/commit/7ee0469ef11fcf46ceaabc5d5c5e609eaccd412e))
* **datatables_select2:** arreglo el asunto de imports js y css ([f8e86f3](https://github.com/ZR-TECDI/zrstats/commit/f8e86f387c597bd826c35f8a9d41737da41635da))
* **datos_iniciales:** pongo los permisos Admin antes de generar_misiones ([70a9cb9](https://github.com/ZR-TECDI/zrstats/commit/70a9cb9fbbb3987e4973d6d52508053b7f4971cc))
* **depends:** bump version de django y pillow por seguridad ([1725c8a](https://github.com/ZR-TECDI/zrstats/commit/1725c8a44dffba5295d338040bf0cd9248277f04))
* **home:** quito imagen de unidad si no estás logueado ([7227a81](https://github.com/ZR-TECDI/zrstats/commit/7227a8141af95d4e00f437351313c4db4bd625b5))
* **imgur:** no deja subir imagenes si no se está logueado ([65b6d1c](https://github.com/ZR-TECDI/zrstats/commit/65b6d1cbad0f969b39ff3030e9a880410029b820))
* **iniciales:** pone campaña solo si la mision es oficial, ignora impros ([5b18575](https://github.com/ZR-TECDI/zrstats/commit/5b185755d1da37ee1cd93d0e052ebbc33609f55f))
* **logics:** ahora la data es capturada correctamente ([ce76acb](https://github.com/ZR-TECDI/zrstats/commit/ce76acb3fe9dd5cf18bc2c16dd81e04cb7cdf2d3))
* **logics:** corregido problema para identificar constantes ([36873de](https://github.com/ZR-TECDI/zrstats/commit/36873de9ce815da8d3adb4a1bacf4783f3cf04cf))
* **migrations:** fix un tema de migraciones y de icono unidad en base ([cd1a56c](https://github.com/ZR-TECDI/zrstats/commit/cd1a56c174a210493dd3daf85af1907a80c554bc))
* **models:** asistencia con miembro on delete cambiado a CASCADE ([22c5d05](https://github.com/ZR-TECDI/zrstats/commit/22c5d052ebd75ee4b13473149fc0647981cae27a))
* **settings:** fix ([47b10b2](https://github.com/ZR-TECDI/zrstats/commit/47b10b277ccd90ec3f9b755499e81ac578e256e4))
* **static:** a esta altura ya es prueba y error ([5e0c278](https://github.com/ZR-TECDI/zrstats/commit/5e0c27839314f2322db9dd4a8d9c72732a33759b))
* **static:** sigo probando arreglar statics ([30f821a](https://github.com/ZR-TECDI/zrstats/commit/30f821a8d35bae31803311130e1792d25e802ece))
* **template:** ancho de tabla en asistencia_mes ([2dfb4ff](https://github.com/ZR-TECDI/zrstats/commit/2dfb4ff22ebb3902aa886108f3b6fbea5cc612a8))
* **template:** arreglo el autoplay del carrousel en home ([2131cb9](https://github.com/ZR-TECDI/zrstats/commit/2131cb98bfe459eff8d32f048208aa8207f5f192))
* **template:** barra superior flotante y padding-top del inner-wrapper ([b48303a](https://github.com/ZR-TECDI/zrstats/commit/b48303a6bd027c9a78e217251e5c038837934db6))
* **template:** correccion nombres de archivo y ocultar titlebar en home ([c1b39f6](https://github.com/ZR-TECDI/zrstats/commit/c1b39f699dd17b14b3934aedd2fe6af5af8c19f6))
* **template:** template de perfiles de usuario ([ebe08f7](https://github.com/ZR-TECDI/zrstats/commit/ebe08f76b309c33d099960d5ba62a8f80c8d8578))
* **template:** template de perfiles de usuario corrección ([5fd509e](https://github.com/ZR-TECDI/zrstats/commit/5fd509e2e96ddd81094d4a19bd2950df2671275d))
* **template:** trabajando en estilo de datatable ([eca4e0b](https://github.com/ZR-TECDI/zrstats/commit/eca4e0b3d858b0efa5879220465a4a9597d80815))
* **urls:** agrego una redireccion automatica a /stats como home ([57ede0e](https://github.com/ZR-TECDI/zrstats/commit/57ede0e9c372e400e12fdc01a152186c49bfbb90))
* **views:** borro una vista que no se usaba ([85c387d](https://github.com/ZR-TECDI/zrstats/commit/85c387d95777a54c4588b238ea4cfab77f8aff50))


### Features

* **asistencia:** mejorada tabla de asistencia mensual ([69b15e6](https://github.com/ZR-TECDI/zrstats/commit/69b15e62d4e71a0bed8bfde9c1c2c1b9f8214080))
* **datatables:** corrección de varias datatables ([c5ab0cd](https://github.com/ZR-TECDI/zrstats/commit/c5ab0cd30ef5cb31f855274d0cba1c2589430073))
* **datos iniciales:** ya procesa el xsl del 2019 ([6684efc](https://github.com/ZR-TECDI/zrstats/commit/6684efc0bb9be71e4e927c8e226b9d3d8b3c5fe9))
* **datos_iniciales:** subo temporalmente los xls y script para leerlos ([1380ff8](https://github.com/ZR-TECDI/zrstats/commit/1380ff869111b3c393c5ab519b2ad41dcef8033d))
* **galeria:** campo autor en galeria ([2627e20](https://github.com/ZR-TECDI/zrstats/commit/2627e20fbfcd01b5a79f36e11b220d90c0dde744))
* **galeria:** loading animation ([6e4c7d4](https://github.com/ZR-TECDI/zrstats/commit/6e4c7d41d70e3546ac2538e3ae5c009d6e4a1d64))
* **home:** agrego mockup de las secciones restantes (datos hardcoded) ([b222261](https://github.com/ZR-TECDI/zrstats/commit/b2222617d4a600b63eb5f861899718b873fd7fa5))
* **home:** fullcalendar funcionando en home ([4b1f0d6](https://github.com/ZR-TECDI/zrstats/commit/4b1f0d6622247690de2725df035f9b102ad27c4d))
* **iniciales:** carga logo de unidad automaticamente ([1d62168](https://github.com/ZR-TECDI/zrstats/commit/1d62168fe52aa556804395215fd9842fdc84a5cc))
* **iniciales:** crea campañas mensuales cuando procesa excel ([466be7e](https://github.com/ZR-TECDI/zrstats/commit/466be7e76edfcdaf6e08544006e7127c23a8c271))
* **logics:** Excepciones personalizadas ([c308ccc](https://github.com/ZR-TECDI/zrstats/commit/c308ccc66071c7d097968bb7a6f30c04181f4b22))
* **miembro:** lista de asistencia en detalle de miembro ([7efb5f3](https://github.com/ZR-TECDI/zrstats/commit/7efb5f30dac0747d752aabed637300bf1c7875ed))
* **models:** campo de imagen en Unidad y Rango ([1fa3a78](https://github.com/ZR-TECDI/zrstats/commit/1fa3a789f4dfeeb0fba73cf2d025343e86b21f05))
* **profile:** linea de tiempo de todo el año con Accordion ([61c46b5](https://github.com/ZR-TECDI/zrstats/commit/61c46b5d2c5e6ea95e1968d5642850378e9545c5))
* **profile:** nuevo panel de porcentaje de asistencia en campaña ([24e02a3](https://github.com/ZR-TECDI/zrstats/commit/24e02a39e2b1aa36cf7621925c022cf9e45ae3db))
* **profile:** prueba de asistencias por tipo de mision y porcentajes ([459a5cd](https://github.com/ZR-TECDI/zrstats/commit/459a5cd4ce8ee97dacaf686f758a8bb97a503d79))
* **profile:** tabla mockup de carrera militar ([dcb7177](https://github.com/ZR-TECDI/zrstats/commit/dcb7177b68e2dd80d9932420c806af658a98c693))
* **template:** barra superior, paneles de home ([86ffb80](https://github.com/ZR-TECDI/zrstats/commit/86ffb80be6923ea75d0f39e7efe73f6d67756e66))
* **template:** carrousel principal en home funcionando ([0260b22](https://github.com/ZR-TECDI/zrstats/commit/0260b22b973f9623dbcbc8308b4f0dd6c6092e7d))
* **template:** detalle de misión ([a1f8ce2](https://github.com/ZR-TECDI/zrstats/commit/a1f8ce29da0d9a70c5dc94c3273584f77f81e628))
* **template:** fotos en home (de prueba por el momento) ([d4b982b](https://github.com/ZR-TECDI/zrstats/commit/d4b982b7396d583ad7cb481162e4186520502762))
* **template:** Hice de cero la barra superior en template BASE ([67f0a87](https://github.com/ZR-TECDI/zrstats/commit/67f0a875ce535d64349054974479d11a08a2e9f6))
* **template:** nos gustaron los headings blancos y sólidos en home ([553a58e](https://github.com/ZR-TECDI/zrstats/commit/553a58e9bbebaea4974006b22b02b3c2ef6fb6be))
* **template:** Pagina de Detalle de Miembro ([360a90c](https://github.com/ZR-TECDI/zrstats/commit/360a90cf2eba47021a023af0b1b1355bf50bd913))
* **template:** parte superior derecha muestra icono de unidad ([16735aa](https://github.com/ZR-TECDI/zrstats/commit/16735aadb11a34c9f959dae0bc514403f8ad19de))
* **template:** prueba de fondo aleatorio en home (template index) ([70939a9](https://github.com/ZR-TECDI/zrstats/commit/70939a93c918b848368153e953abeb50a00b7639))

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
