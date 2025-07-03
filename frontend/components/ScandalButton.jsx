// ScandalButton.jsx
import React from "react";
export default function ScandalButton({ onClick }) {
  return (
    <button
      className="bg-green-700 hover:bg-green-900 text-white px-6 py-3 rounded-2xl shadow-xl"
      onClick={onClick}
    >
      🚨 زر الفضيحة السيبرانية 🚨
    </button>
  );
}
