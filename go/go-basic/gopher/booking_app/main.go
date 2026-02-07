package main
import "fmt"
import "strings"

func main() {
	var conferenceName string = "Go Conference"
	var remainingTickets uint16 = 50
	const conferenceTickets int = 50
	var bookings []string

	fmt.Printf("Welcome to %v booking application\n", conferenceName)
	fmt.Printf("We have a total of %v and %v are still remaining, ", conferenceTickets, remainingTickets)
	fmt.Println("Get your tickets here to attend ")

	for {
	var firstName string
	var lastName string
	var email string
	var userTickets uint16

	fmt.Println("Enter your first name:")
	fmt.Scan(&firstName)
	fmt.Println("Enter your last name: ")
	fmt.Scan(&lastName)
	fmt.Println("Enter your email: ")
	fmt.Scan(&email)
	fmt.Println("Enter number of Tickets: ")
	fmt.Scan(&userTickets)

	if userTickets > remainingTickets {
		fmt.Printf("We only have %v Tickets\n Please Try Again!\n", remainingTickets)
		continue
	}

	remainingTickets = remainingTickets - userTickets
 	bookings = append(bookings, firstName + " " + lastName)

	firstNames := []string{}
	names := []string{}
	for index, booking := range bookings {
		names = strings.Fields(booking)
		firstName = names[index]
		firstNames = append(firstNames, firstName)
	}


	fmt.Printf("Hello %v, thank you for registering for the %v \nYour email is %v\nNumber of Tickets bought: %v\nRemaining Tickets %v\n", bookings[0], conferenceName, email, userTickets, remainingTickets)
	fmt.Printf("%v\n", firstNames)

	if remainingTickets == 0 {
		fmt.Println("Tickets have been depleted!")
		break
	}
}
}
