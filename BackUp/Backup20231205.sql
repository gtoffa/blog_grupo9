-- MySQL dump 10.13  Distrib 8.0.34, for Linux (x86_64)
--
-- Host: localhost    Database: blog_grupo9
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `noticias_categoria`
--

DROP TABLE IF EXISTS `noticias_categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `noticias_categoria` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `noticias_categoria`
--

LOCK TABLES `noticias_categoria` WRITE;
/*!40000 ALTER TABLE `noticias_categoria` DISABLE KEYS */;
INSERT INTO `noticias_categoria` VALUES (1,'Relatos'),(2,'Emigrar'),(3,'Bancos, Dinero, Tarjetas'),(4,'Alojamiento'),(5,'Alquiler Auto');
/*!40000 ALTER TABLE `noticias_categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `noticias_noticia`
--

DROP TABLE IF EXISTS `noticias_noticia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `noticias_noticia` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `titulo` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `contenido` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `imagenes` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `fecha_publicacion` datetime(6) NOT NULL,
  `categoria_noticia_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `noticias_noticia_categoria_noticia_id_d2503edd_fk_noticias_` (`categoria_noticia_id`),
  CONSTRAINT `noticias_noticia_categoria_noticia_id_d2503edd_fk_noticias_` FOREIGN KEY (`categoria_noticia_id`) REFERENCES `noticias_categoria` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `noticias_noticia`
--

LOCK TABLES `noticias_noticia` WRITE;
/*!40000 ALTER TABLE `noticias_noticia` DISABLE KEYS */;
INSERT INTO `noticias_noticia` VALUES (1,'Planeaba aterrizar en Barcelona e ir hasta Cadaqués en bus, pero me estoy arrepintiendo','Estoy planeando un próximo viaje a Europa desde Argentina. La primera etapa de ese viaje se desarrollará en España, más específicamente en Cataluña, ya tengo emitido el vuelo de ida a Barcelona.\r\n\r\nLlegaré al Aeropuerto Josep Tarradellas Barcelona-El Prat (BCN) por la mañana y, desde allí, pensaba tomar un bus hacia la localidad costera de Cadaqués, en el noreste de Cataluña. Me imaginaba que entre una cosa y otra me llevaría unas cuatro horas llegar a mi primer destino.\r\n\r\nPensé ir en bus porque, en una búsqueda sencilla, vi que había una línea de bus desde el Aeropuerto de Barcelona a Cadaqués y porque quizás llegaría un poco cansado luego de un viaje intercontinental como para manejar unas horas en una ruta que no conozco.\r\n\r\nPero ahora, avanzando un poco más en firme con los planes, la idea de alquilar un auto comienza a seducirme. Llego, retiro el auto en el aeropuerto, emprendo el viaje hacia Cadaqués, paro en algún buen lugar en la ruta a tomar algo. Somos dos personas que manejamos, así que si una se cansa, la otra toma la posta, dicen que el camino el muy lindo… Sí, alquilar un auto empieza a parecer una buena idea.\r\n\r\nAdemás me contacté con el alojamiento y me dijeron que se puede dejar el auto ahí mismo, en la calle, de manera gratuita (vamos en temporada baja).\r\n\r\nTambién pienso ir a Figueres, a Girona, recorrer los alrededores y luego volver a Barcelona; mientras escribo esto me convenzo cada vez más.\r\n\r\nMe puse a mirar en Bookingcars (que ofrece 5% de descuento a nuestros lectores ingresando el código INFOVIAJERA) y encontré opciones con todos los seguros incluidos (sin franquicia) y conductor adicional sin cargo, así que me parece que me termino de decidir y andaré ruteando a mi ritmo por Cataluña, despreocupado de los horarios de los transportes públicos, de las reglas para el equipaje y cosas por el estilo.\r\n\r\nEn un viaje reciente alquilé auto al llegar a Barcelona, y resultó sencillo y muy conveniente. Aquí les contábamos un poco:\r\n\r\nY ustedes,\r\n\r\nEn este tipo de viajes, ¿prefieren moverse en auto o utilizar trenes o buses?\r\n\r\nActualización luego de haber leídos sus comentarios:','noticias/Devolver-Auto-Alquilado-Aeropuerto-de-Barcelona-Estacionamiento_RJeniKJ.webp','2023-12-05 23:47:07.154792',5),(2,'Un maravilloso almuerzo en el Hotel Llao Llao de Bariloche (Argentina)','En el mes de octubre nos hicimos una escapada a Bariloche, mejor dicho, al famoso Hotel Llao Llao, pues prácticamente estuvimos todo el tiempo en el hotel y su maravilloso entorno natural.\r\n\r\nEn este post les contaremos sobre una de las experiencias en el hotel: el almuerzo buffet Salad Bar en el precioso Winter Garden.\r\n\r\nAquí vemos el lobby bar del hotel, sobre el final está el Winter Garden.\r\n\r\n \r\n\r\nFinalmente pasamos a ese sector y nos acomodamos en nuestra mesa, belleza por doquier.\r\n\r\nEl sistema es así: se paga un importe fijo que incluye una bebida sin alcohol, otra bebida con alcohol, un impresionante buffet frío, sopas, platos principales calientes, postres y café con petit fours. En este momento el precio es de AR$ 25.500 (unos USD 26 por persona).\r\n\r\nDesde ya les aviso que me dediqué a disfrutar del Salad Bar y puse atención en hacer un video en el que les muestro detalladamente toda la experiencia, pero no tomé tantas fotos. Les sugiero que miren el video que dejo sobre el final del post.\r\n\r\nAsí lucía mi plato luego de la primera incursión al buffet frío:\r\n\r\nLuego, el plato principal, un exquisito bife de chorizo con una salsa que estaba como para chuparse los dedos.\r\n\r\nNo hay foto de la sopita de arvejas y pera que disfruté \r\n\r\nA la hora del postre, tuve que probar los milhojas de chocolate:\r\n\r\n\r\nY también los frutos rojos con crema y salsa de chocolate:\r\n\r\nFuimos cerrando el almuerzo con un cafecito con petit fours:\r\n\r\nEntre una cosa y otra, estuvimos dos horas disfrutando de este almuerzo Salad Bar en el Winter Garden. Hubo una combinación de factores que conformaron una experiencia realmente muy especial, voy a intentar descomponer algunos:\r\n\r\nLugar soñado: el Winter Garden es una belleza. Un espacio amplio, vidriado, muy bien decorado, con mesas muy bien dispuestas, excelente mobiliario y preciosa y tradicional vajilla.\r\nSabores, sabores, y sabores: la gastronomía del Llao Llao es de esas que nos arrancan exclamaciones. Todo estaba excelente: el salmón ahumado con alcaparras, las ensaladas con burrata, pera y hojas verdes, el chocolate del milhojas…\r\nVariedad: ahora que estoy haciendo el artículo y revisando el material, me lamento al recordar que había tantas cosas es en ese maravilloso buffet que me quedaron varias sin probar, ¡voy a tener que volver!\r\nServicio: la amable y profesional atención del personal del Llao Llao se nota en cada detalle, por ejemplo al brindar opciones para personas con necesidades alimentarias especiales.\r\n\r\nEn el siguiente video les contamos con más detalle acerca de la experiencia en el Salad Bar en el Winter Garden del Hotel Llao Llao de Bariloche:','noticias/Lobby-Bar-Hotel-Llao-Llao-Bariloche-Argentina_iDWJ20m.webp','2023-12-05 23:52:06.747181',1),(3,'Promos para estudiar y trabajar en el extranjero (Irlanda, Malta, USA y más)','En Info Viajera siempre estamos buscando formas de viajar y conocer el mundo. Una que a mí particularmente me gusta mucho es combinar un destino con estudio y/o trabajo.\r\n\r\nEn esa búsqueda, recientemente conocimos a GrowPro, una empresa española que se especializa en acompañar a personas que quieren ir a estudiar inglés en Australia, Nueva Zelanda, Canadá, Malta e Irlanda, así como también trabajar y desarrollarse académicamente en varios países.\r\n\r\nSegún venimos viendo, cada mes publican diversas promociones en sus experiencias, tanto de trabajo, estudio o una combinación de ambas. Por ejemplo, ahora en octubre lanzaron como novedad una MUY buena oferta para ir a trabajar como Au Pair en Estados Unidos. Si bien está disponible solo para mujeres menores de 26 años y de algunas nacionalidades, no deja de ser una actividad que acerca a la cultura del lugar y el idioma, mientras que permite ahorrarse el alojamiento y ganar dinero.\r\n\r\nPara quienes están buscando irse un buen tiempo a Europa y mejorar su inglés, los cursos de 25 semanas en Irlanda siguen siendo una excelente oportunidad. El datazo: al contratar un curso de esta duración, te dan un permiso de trabajo, incluso si no tenés ciudadanía europea.\r\n\r\nEn este artículo, explican todas las maneras de emigrar a Irlanda, ya sea por seis meses o más tiempo: https://growproexperience.com/irlanda/emigrar-a-irlanda\r\n\r\nY vos,\r\n\r\n¿Estás pensando en ir a vivir una experiencia al extranjero? ¿Emigrar? ¿Estudiar y trabajar?\r\n\r\nLinks de interés:\r\n\r\nPromos en la web de GrowPro\r\nEstudiando en el exterior: mi experiencia en Londres (Inglaterra)','noticias/Dublin-Estatua-Molly-Malone-Irlanda-Centro.webp','2023-12-05 23:54:10.856923',2);
/*!40000 ALTER TABLE `noticias_noticia` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-05 21:48:59
