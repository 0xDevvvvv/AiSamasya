"use client";
import Image from "next/image";
import React, { useState, useEffect } from "react";
import {
  FiUser,
  FiSettings,
  FiPhone,
  FiVideo,
  FiSend,
  FiPaperclip,
  FiSmile,
} from "react-icons/fi";
import { format } from "date-fns";

export default function Home() {
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState("");
  const [isTyping, setIsTyping] = useState(false);

  const currentUser = {
    id: 1,
    name: "AD to PD",
    avatar:
      "data:image/png;base64,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",
    followers: 1200,
    posts: 87,
    bio: "Photography enthusiast | Travel lover",
    location: "New York, USA",
  };

  const otherUser = {
    id: 2,
    name: "maths exam",
    avatar:
      "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSY_J3Gd1goUDTW8ZBSFU0K1iZCzP4GcSl3zxeOQ3xajpoF4Gi2tl3M2b7Ryl-bM2DGVQU&usqp=CAU",
    followers: 3500,
    posts: 152,
    bio: "Digital artist | Coffee addict",
    location: "Los Angeles, USA",
  };

  useEffect(() => {
    // Simulating initial messages
    setMessages([
      {
        id: 1,
        sender: otherUser,
        content: "Hey there!",
        timestamp: new Date(Date.now() - 3600000),
      },
      {
        id: 2,
        sender: currentUser,
        content: "Hi! How are you?",
        timestamp: new Date(Date.now() - 3540000),
      },
      {
        id: 3,
        sender: otherUser,
        content: "I'm good, thanks! How about you?",
        timestamp: new Date(Date.now() - 3480000),
      },
    ]);
  }, []);

  const handleSendMessage = () => {
    if (inputMessage.trim() !== "") {
      const newMessage = {
        id: messages.length + 1,
        sender: currentUser,
        content: inputMessage,
        timestamp: new Date(),
      };
      setMessages([...messages, newMessage]);
      setInputMessage("");
      setIsTyping(false);
    }
  };

  const handleInputChange = (e) => {
    setInputMessage(e.target.value);
    setIsTyping(e.target.value.trim() !== "");
  };

  return (
    <div className="flex h-screen bg-gray-900 text-white">
      <div className="w-1/4 bg-gray-800 p-4 border-r border-gray-700">
        <div className="flex items-center justify-between mb-6">
          <div className="flex items-center">
            <img
              src={currentUser.avatar}
              alt={currentUser.name}
              className="w-10 h-10 rounded-full mr-3"
            />
            <span className="font-semibold">{currentUser.name}</span>
          </div>
          <div className="flex space-x-2">
            <button className="p-2 rounded-full hover:bg-gray-700 transition-colors duration-200">
              <FiSettings className="w-5 h-5" />
            </button>
          </div>
        </div>
        <input
          type="text"
          placeholder="Search conversations..."
          className="w-full bg-gray-700 text-white rounded-full py-2 px-4 mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <div className="space-y-4">
          {/* Conversations list would go here */}
          <div className="flex items-center p-2 rounded-lg hover:bg-gray-700 transition-colors duration-200 cursor-pointer">
            <img
              src={otherUser.avatar}
              alt={otherUser.name}
              className="w-12 h-12 rounded-full mr-3"
            />
            <div>
              <h3 className="font-semibold">{otherUser.name}</h3>
              <p className="text-sm text-gray-400">Last message...</p>
            </div>
          </div>
        </div>
      </div>
      <div className="flex-1 flex flex-col">
        <div className="bg-gray-800 p-4 flex items-center justify-between">
          <div className="flex items-center">
            <img
              src={otherUser.avatar}
              alt={otherUser.name}
              className="w-10 h-10 rounded-full mr-3"
            />
            <div>
              <h2 className="font-semibold">{otherUser.name}</h2>
              <p className="text-sm text-gray-400">
                {otherUser.followers} followers • {otherUser.posts} posts
              </p>
            </div>
          </div>
          <div className="flex space-x-4">
            <button className="p-2 rounded-full hover:bg-gray-700 transition-colors duration-200">
              <FiPhone className="w-5 h-5" />
            </button>
            <button className="p-2 rounded-full hover:bg-gray-700 transition-colors duration-200">
              <FiVideo className="w-5 h-5" />
            </button>
            <button className="p-2 rounded-full hover:bg-gray-700 transition-colors duration-200">
              <FiUser className="w-5 h-5" />
            </button>
          </div>
        </div>
        <div className="flex-1 overflow-y-auto p-4 space-y-4">
          {messages.map((message) => (
            <div
              key={message.id}
              className={`flex ${
                message.sender.id === currentUser.id
                  ? "justify-end"
                  : "justify-start"
              }`}
            >
              <div
                className={`max-w-xs lg:max-w-md xl:max-w-lg ${
                  message.sender.id === currentUser.id
                    ? "bg-blue-600"
                    : "bg-gray-700"
                } rounded-lg p-3 shadow-md`}
              >
                <p>{message.content}</p>
                <p className="text-xs text-gray-400 mt-1">
                  {format(message.timestamp, "p")}
                </p>
              </div>
            </div>
          ))}
        </div>
        <div className="bg-gray-800 p-4">
          <div className="flex items-center bg-gray-700 rounded-full">
            <button className="p-2 rounded-full hover:bg-gray-600 transition-colors duration-200">
              <FiPaperclip className="w-5 h-5" />
            </button>
            <input
              type="text"
              value={inputMessage}
              onChange={handleInputChange}
              placeholder="Type a message..."
              className="flex-1 bg-transparent py-2 px-4 focus:outline-none"
            />
            <button className="p-2 rounded-full hover:bg-gray-600 transition-colors duration-200">
              <FiSmile className="w-5 h-5" />
            </button>
            <button
              onClick={handleSendMessage}
              className="p-2 rounded-full bg-blue-500 hover:bg-blue-600 transition-colors duration-200 ml-2"
            >
              <FiSend className="w-5 h-5" />
            </button>
          </div>
          {isTyping && <p className="text-sm text-gray-400 mt-1">Typing...</p>}
        </div>
      </div>
    </div>
  );
}
