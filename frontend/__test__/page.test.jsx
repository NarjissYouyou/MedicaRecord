import '@testing-library/jest-dom'
import { render, screen } from '@testing-library/react'
import Home from '../app/page'
 
describe('Home component', () => {
  it('renders the text "Medica Record"', () => {
    render(<Home />);

    // Check if the text "Medica Record" is in the document
    const textElement = screen.getByText('Medica Record');
    expect(textElement).toBeInTheDocument();
  })
})