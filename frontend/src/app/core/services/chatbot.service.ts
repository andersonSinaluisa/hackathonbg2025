import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { API_URL } from '../../shared/constants';

import { firstValueFrom, Observable } from 'rxjs';

export interface ChatResponse{
  message: string;
}

@Injectable({
  providedIn: 'root'
})
export class ChatbotService {
  module_api_segment = 'chat/';
  tokenHttpServiceUrl = 'http://localhost:8000/'+this.module_api_segment;


  constructor(private httpClient: HttpClient) { }

  async sendMessage(userId: string, message: string): Promise<ChatResponse> {
    console.log(this.tokenHttpServiceUrl);
    console.log({user_id:userId, message:message})
    const response = await firstValueFrom(this.httpClient.post<ChatResponse>(`${this.tokenHttpServiceUrl}`,{user_id:userId, message:message}));
    console.log(response)
    return response
  }

}
