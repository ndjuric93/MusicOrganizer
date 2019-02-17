import React from 'react';

const footerStyle = {
    position: "fixed",
    left: "0px",
    bottom: "0px",
    paddingLeft: "200px",
    paddingBottom: "0px",
    width: "100%"
  };
  
export default function Footer({ children }) {
    return (
      <div>
        <div style={footerStyle}>{children}</div>
      </div>
    );
}