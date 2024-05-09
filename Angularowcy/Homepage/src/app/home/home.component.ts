 import { Component } from '@angular/core';
import { Title } from '@angular/platform-browser';
import { ContactComponent } from '../contact/contact.component';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [ContactComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {

  constructor(private titleService: Title) {
    this.titleService.setTitle('Ardium - Home');
  }
}
