# Список заданий для выполнения
 
+ Приведите пример калибровки с шаблоном в виде круга (на собственном видео)    

Данный код выполняет калибровку камеры на основе изображений с круговыми объектами. Он использует детектор SimpleBlobDetector для поиска круговых объектов на каждом изображении, затем находит среди них шаблон в виде шахматной доски. Функция findCirclesGrid находит на изображении узлы шахматной доски. 

Сначала задаются параметры детекции круговых объектов SimpleBlobDetector_Params, включая пороговые значения, минимальную и максимальную площадь, минимальную циркулярность, минимальную выпуклость и минимальное отношение инерции. Затем создается детектор круговых объектов blobDetector с заданными параметрами, а также определяется трехмерная позиция круговых объектов на шахматной доске.

Далее код определяет путь к файлам изображений, получает список файлов в директории  *"../data/calib"* и загружает каждое изображение на этапе поиска углов шахматной доски. Обнаруживает круговые объекты, используя детектор blobDetector, и ищет шаблон шахматной доски на изображении с помощью функции findCirclesGrid, получая координаты доски в 3D (objpoints) и соответствующие 2D координаты углов на изображении (imgpoints).

Затем на изображении отрисовываются найденные углы шахматной доски и выводится для проверки.

+ Приведите пример калибровки по тегам aprilGrid (на собственном видео)  
+ Визуализируйте движение камеры относительно шаблона  
+ Визуализируйте положение шаблона относительно камеры