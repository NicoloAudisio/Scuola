import React from 'react';

class ScrollToTopButton extends React.Component {
  scrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth"
    });
  };

  render() {
    return (
      <button onClick={this.scrollToTop}>
        Torna in cima
      </button>
    );
  }
}

export default ScrollToTopButton;