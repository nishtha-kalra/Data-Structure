type Order = {
  price: number;
  quantity: number;
};

class OrderBook {
  bids: Order[] = []; // An array of buy orders.
  asks: Order[] = []; // An array of sell orders.

  addBids(price: number, quantity: number) {
    this.bids.push({price, quantity}); //adds a new bid (buy order) to the bids array
    this.bids.sort((a, b) => b.price - a.price); // sorts in descending order
  }

  addAsks(price: number, quantity: number) {
    this.asks.push({price, quantity});
    this.asks.sort((a, b) => a.price - b.price); //sorts in ascending order
  }

  matchOrders() {
    while(this.bids.length && this.asks.length) {
      const buyOrder = this.bids[0];
      const sellOrder = this.asks[0];

      if (buyOrder.price >= sellOrder.price) {
        const quantity = Math.min(buyOrder.quantity, sellOrder.quantity);
        buyOrder.quantity -= quantity;
        sellOrder.quantity -= quantity;

        if (buyOrder.quantity == 0) {
          this.bids.shift();
        }
        if (sellOrder.quantity == 0) {
          this.asks.shift();
        }
      } else {
        break;
      }
    }
  }

  calculateDepth(limit: number) {
    let bidsDepth: number = 0;
    let asksDepth: number = 0;

    for (let i = 0; i < Math.min(limit, this.bids.length); i ++) {
      bidsDepth += this.bids[i].quantity;
    }

    for (let i = 0; i < Math.min(limit, this.asks.length); i ++) {
      asksDepth += this.asks[i].quantity;
    }

    console.log('Asks depth:', asksDepth);
    console.log('Bids depth:', bidsDepth);
  }

  printOrderBook() {
    console.log('Bids:');
    this.bids.forEach(bid => console.log(`Price: ${bid.price}, Quantity: ${bid.quantity}`));
    console.log('Asks:');
    this.asks.forEach(ask => console.log(`Price: ${ask.price}, Quantity: ${ask.quantity}`));
  }
}

const orderBook = new OrderBook();
orderBook.addBids(30000, 2);
orderBook.addBids(29500, 1);
orderBook.addBids(29000, 1.5);
orderBook.addBids(28500, 2);
orderBook.addBids(28000, 1);

orderBook.addAsks(30500, 1.5);
orderBook.addAsks(31000, 2);
orderBook.addAsks(31500, 1);
orderBook.addAsks(32000, 1.5);
orderBook.addAsks(32500, 2);
console.log('before match:');
orderBook.printOrderBook();
orderBook.matchOrders();
console.log('after match:');
orderBook.printOrderBook();
orderBook.calculateDepth(3);