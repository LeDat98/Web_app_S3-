const texts = ['Cluttered house in the woods | anime oil painting high resolution cottagecore ghibli inspired 4k',
        'environment living room interior, mid century modern, indoor garden with fountain, retro,m vintage, designer furniture made of wood and plastic, concrete table, wood walls, indoor potted tree, large window, outdoor forest landscape, beautiful sunset, cinematic, concept art, sunstainable architecture, octane render, utopia, ethereal, cinematic light, -ar 16:9 -stylize 45000',
        'A digital illustration of the Babel tower, 4k, detailed, trending in artstation, fantasy vivid colors','house in the mountain fujisan japan,| anime oil painting high resolution cottagecore ghibli inspired 4k',
        'futuristic nighttime cyberpunk New York City skyline landscape vista photography by Carr Clifton & Galen Rowell, 16K resolution, Landscape veduta photo by Dustin Lefevre & tdraw, 8k resolution, detailed landscape painting by Ivan Shishkin, DeviantArt, Flickr, rendered in Enscape, Miyazaki, Nausicaa Ghibli, Breath of The Wild, 4k detailed post processing, atmospheric, hyper realistic, 8k, epic composition, cinematic, artstation —ar 16:9','A digital illustration of a steampunk library with clockwork machines, 4k, detailed, trending in artstation, fantasy vivid colors,',
        'The green idyllic Arcadian prairie with sheep by Thomas Cole, Breath-taking digital painting with placid colours, amazing art, artstation 3, cottagecore',
        'Style1 a jungle, super magical nature, fresh light, clear colors, lush flowers, flying yellow butterflies, green river in the middle,A digital illustration of a Style1 a jungle, super magical nature, fresh light, clear colors, lush flowers, flying yellow butterflies, green river in the middle with clockwork machines, 4k, detailed, trending in artstation, fantasy vivid colors',
        'Style2 Tokyo city with TokyoTower tower, in the warm sunset afternoon, the light is warm and clear, in the distance is Mount Fujisan,| anime oil painting high resolution cottagecore ghibli inspired 4k',
        'Style2 Japanese village scenery, fields, green hills, flowing river, small houses, far away is mount fujisan, beautiful sunset landscape,| anime oil painting high resolution cottagecore ghibli inspired 4k,| anime oil painting high resolution cottagecore ghibli inspired 4k',
        'Style3 French-style living room, motifs with classic patterns are always emphasized with unique sophistication, neutral colors yellow white beige, diverse pillar system, spacious arched doors and the shapes come out clearly,mid century modern, indoor garden with fountain, retro,m vintage, designer furniture made of wood and plastic, concrete table, wood walls, indoor potted tree, large window, outdoor forest landscape, beautiful sunset, cinematic, concept art, sunstainable architecture, octane render, utopia, ethereal, cinematic light, -ar 16:9 -stylize 45000',
        'Style3 spacious and airy Italian style living room design,large space, deep brown sofa, small wooden table, gray wall with luxurious wood pattern, vase with green leaves, black wall with luxurious wood grain pattern, glass door in full wall, garden beautiful green,mid century modern, indoor garden with fountain, retro,m vintage, designer furniture made of wood and plastic, concrete table, wood walls, indoor potted tree, large window, outdoor forest landscape, beautiful sunset, cinematic, concept art, sunstainable architecture, octane render, utopia, ethereal, cinematic light, -ar 16:9 -stylize 45000',
        'Style1 the ancient library is located in the middle of a mysterious forest, luxuriant trees and many flowers and butterflies fluttering, mysterious light, golden light,,A digital illustration of a Style1 the ancient library is located in the middle of a mysterious forest, luxuriant trees and many flowers and butterflies fluttering, mysterious light, golden light, with clockwork machines, 4k, detailed, trending in artstation, fantasy vivid colors'];
function randomText() {
// Lấy ngẫu nhiên một dòng văn bản từ mảng texts
const randomIndex = Math.floor(Math.random() * texts.length);
const randomText = texts[randomIndex];
          
// Đưa dòng văn bản ngẫu nhiên vào tag input
document.getElementById('input').value = randomText;
}
// tải ảnh từ nút
const buttons = document.querySelectorAll('button');
const images = document.querySelectorAll('img');

buttons.forEach(function(button, index) {
button.addEventListener('click', function() {
const image = images[index];
const imageUrl = image.getAttribute('src');
// Tải hình ảnh từ đường dẫn có trong thẻ img
// Bạn có thể sử dụng ajax hoặc fetch API để tải hình ảnh
});
});
