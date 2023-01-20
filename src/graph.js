export class Graph {
  constructor(is_directed = true) {
    this.edges = new Map()
    this.traits = {
      is_directed: is_directed
    }
  }

  edge(from, to, weight = 1) {
    Graph._Private._edge(this, from, to, weight)

    if (this.traits.is_directed === false) {
      Graph._Private._edge(this, to, from, weight)
    }

    return this
  }

  static _Private = {
    _edge(_this, from, to, weight) {
      const tos = _this.edges.get(from)

      if (tos === undefined) {
        _this.edges.set(from, new Map([[to, weight]]))
      } else {
        tos.set(to, weight)
      }
    }
  }
}

console.log(new Graph().edge(1,2).edge(2,3).edge(1,3))
