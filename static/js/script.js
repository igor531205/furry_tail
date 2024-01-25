// document.addEventListener('DOMContentLoaded', function() {
//     document.querySelectorAll('.card').forEach(function(card) {
//         console.log(card);
//         card.addEventListener('click', function() {
//             let detailsDiv = this.querySelector('.details');
//             console.log(detailsDiv);
//             let largePhoto = detailsDiv.querySelector('.largePhoto');
//             let descriptionParagraph = detailsDiv.querySelector('.fakeText');
            
//             // Копируем src из маленького изображения в большое
//             let smallPhotoSrc = this.querySelector('.photo img').src;
//             largePhoto.src = smallPhotoSrc;

//             // Переключаем отображение блока с деталями
//             detailsDiv.style.display = detailsDiv.style.display === 'none' ? 'flex' : 'none';

//             // Убираем загрузку текста из API, используем описание животного
//             // descriptionParagraph.innerHTML уже содержит {{ animal.description }}

//             detailsDiv.addEventListener('click', function(event) {
//                 this.style.display = 'none';
//                 event.stopPropagation(); // Предотвращаем всплытие события к карточке
//             });
//         });
//     });
// });
