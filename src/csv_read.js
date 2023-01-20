import { parse } from 'csv';
import { readFile } from 'fs/promises';
import { Graph } from './graph.js';

const input = await readFile('./input/bitcoinalpha.csv')
const g = new Graph(true)

const parser = 
  parse({delimiter: ','})
  .on('readable', () => {
    for (let row; (row = parser.read()); ) {
      g.edge(row[1], row[2], row[3])
    }
  })
  .on('error', (err) => {
    console.error(err.message)
  })
  .on('end', () => {
    for (let [from, tos] of g.edges) {
      let list = []
      for (let [to, weight] of tos) {
        list.push(to)
      }
      console.log(from, list)
    }
  })

parser.write(input)
parser.end()
