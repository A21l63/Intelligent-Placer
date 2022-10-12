# intelligent-placer
## Постановка задачи
"Intelligent placer" - программа, определяющая по поданной на вход фотографии нескольких предметов на горизонтальной поверхности и многоугольнику, можно ли расположить одновременно все эти предметы на плоскости так, чтобы они влезли в этот многоугольник.

### Ввод\Вывод
*Ввод:* 
Изображение в формате *.jpg, состоящее из предметов и многоугольника, изображенного на белом листе бумаги, расположенном в правой части фотографии (это необходимо для того, чтобы парсить ). Сами объекты должны быть отчетливо различимы на белой поверхности и расположены в правой части изображения.

*Вывод:* 
Если можно разместить - **True**
В противном случае - **False**

## Требования
### Общие:
- Формат: jpg/jpeg/png фотография
- Камера направлена по направлению антинормали (отклонение не более 10-15 градусов) к поверхности для предотвращения значимых перспективных искаженией
- По краям изображения не должно быть большой площади пустой поверхности без объектов
### К объектам:
- Объекты должны иметь размер, достаточный для того, чтобы их границы можно было определить по фотографии
- Габариты объектов не должны значительно превышать оных у листа, ибо тогда задача автоматически не имеет смысла 
- Границы объектов должны быть определимы (не должно быть очень мелких деталей)
- Объекты не должны вылезать за границы изображения
- В кадре не должно быть частей посторонних объектов
- В объектах не должно быть прозрачных частей
### К освещению:
- Освещение должно быть монотонным
- Освещение должно иметь равную интенсивность на всех участках фотографии
- Не должно создаваться бликов, видимых на фотографии
- Освещение не должно создавать теней, которые могут быть приняты за продолжение объектов
### К многоугольнику и листу бумаги
- Лист бумаги с многоугольником может располагаться в любой части экрана с любым углом поворота
- Пропоции листа не должны быть искажены
- Границы листа должны быть четко определимы
- Многоугольник должен быть выпуклым (это условие обусловлено моим текущим пониманием того, как буду решать задачу)
- Границы многоугольника должы быть четко определимы
### К поверхности
- Поверхность не должна создавать бликов и отражений
- Желательно, чтобы поверхность была матовой
- Поверхность не должна обладать рельефом, тень от которого может повлечь за собой искажения в определении границ объектов
