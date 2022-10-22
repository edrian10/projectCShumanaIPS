const app = document.getElementById('typewriter')
;
const typewriter = new Typewriter(app,{
    loop: true,
    delay:75
});

typewriter
.typeString('Barrio San Marcos')
.pauseFor(200)
.start();