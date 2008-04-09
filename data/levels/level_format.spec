Level object:
{
  "id"       : "",
  "placed"   : [
                 {
                   "type" : "object type",
                   "name" : "object name",
                   "xpos" : "x position, from topleft",
                   "ypos" : "y position, from topleft"
                 }
               ],
  "available": [
                 {
                   "type" : "object type",
                   "name" : "object name"
                 }
               ],
  "goals"    : [
                 ["projectile object name", "target object name"]
               ],
  "help"     : "filename"
}

An example:
{
  "id"       : "first level",
  "placed"   : [
                 {
                   "type" : "SoccerBall",
                   "name" : "bola",
                   "xpos" : "200",
                   "ypos" : "300"
                 },
                 {
                   "type" : "Esteira",
                   "name" : "rolante",
                   "xpos" : "300",
                   "ypos" : "500"
                 },
                 {
                   "type" : "Target",
                   "name" : "alvo",
                   "xpos" : "1000",
                   "ypos" : "600"
                 }
               ],
  "available": [
                 {
                   "type" : "Penguin",
                   "name" : "tux"
                 }
               ],
  "goals"    : [
                 ["bola", "alvo"]
               ],
  "help"     : "help1.png"
}
