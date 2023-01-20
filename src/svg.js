import { SVG } from '@svgdotjs/svg.js'
var draw = SVG().addTo('body').size(300, 300)
var rect = draw.rect(100, 100).animate({
  duration: 2000,
  delay: 1000,
  when: 'now',
  swing: true,
  times: 5,
  wait: 200
}).attr({ fill: '#f06' })