import { Component, OnInit, OnDestroy } from '@angular/core';
import {MatCardModule} from '@angular/material/card';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { ChatbotService } from '../../core/services/chatbot.service';

interface Message {
  text: string;
  sender: 'user' | 'bot';
}

@Component({
  selector: 'app-chatbot',
  standalone: true,
  template: `
    <div class="flex flex-col h-screen p-4 bg-gray-100">
      <div class="flex-grow overflow-auto p-4 bg-white rounded shadow-md">
        <div *ngFor="let msg of messages" [ngClass]="{'text-right': msg.sender === 'user', 'text-left': msg.sender === 'bot'}" class="mb-2">
          <span [ngClass]="{'bg-blue-500 text-white': msg.sender === 'user', 'bg-gray-300 text-black': msg.sender === 'bot'}" class="px-4 py-2 rounded-lg inline-block">{{ msg.text }}</span>
        </div>
      </div>
      <div class="mt-4 flex">
        <input [(ngModel)]="userInput" (keyup.enter)="sendMessage()" class="flex-grow p-2 border rounded" placeholder="Type a message...">
        <button (click)="sendMessage()" class="ml-2 px-4 py-2 bg-blue-500 text-white rounded">Send</button>
      </div>
    </div>
  `,
  imports:[MatCardModule,ReactiveFormsModule, CommonModule,FormsModule],
  styles: []
})
export class ChatbotComponent {
  messages: Message[] = [];
  userInput: string = '';

  constructor(private chatbotService: ChatbotService) {}

  sendMessage() {
    if (!this.userInput.trim()) return;
    const userMessage: Message = { text: this.userInput, sender: 'user' };
    this.messages.push(userMessage);

    this.chatbotService.sendMessage('0932006802',userMessage.text).then(response => {
      console.log('response',response)
      this.messages.push({ text: response.message, sender: 'bot' });
    });

    this.userInput = '';
  }
}
