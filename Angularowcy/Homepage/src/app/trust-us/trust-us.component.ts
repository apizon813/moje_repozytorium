import { CommonModule, NgFor } from '@angular/common';
import { Component, OnDestroy, OnInit } from '@angular/core';

@Component({
  selector: 'app-trust-us',
  standalone: true,
  imports: [CommonModule, NgFor],
  templateUrl: './trust-us.component.html',
  styleUrl: './trust-us.component.css'
})
export class TrustUsComponent implements OnInit, OnDestroy{
  currentIndex: number = 0;
  changeInterval: number = 3000;
  intervalId: any;

  ngOnInit(): void {
    this.intervalId = setInterval(() => {
      this.showNextItem();
    }, this.changeInterval);
  }

  ngOnDestroy(): void {
    if (this.intervalId) {
      clearInterval(this.intervalId);
    }
  }

  showNextItem(): void {
    this.currentIndex = (this.currentIndex + 1) % 3;
  }
}