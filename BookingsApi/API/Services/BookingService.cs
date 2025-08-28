using BookingsApi.Interfaces;
using BookingsApi.Models;

namespace BookingsApi.Services
{
    public class BookingService(IBookingRepository bookingRepository) : IBookingService
    {
        private readonly IBookingRepository _repo = bookingRepository;

        public IEnumerable<Booking> GetAll() => _repo.GetAll();

        public Booking? GetById(int id) => _repo.GetById(id);

        /// <summary>
        /// Returnerar true om tidsintervallet krockar med befintlig bokning
        /// </summary>
        public bool HasOverlap(int roomId, DateTime from, DateTime to)
        {
            return _repo.GetAll().Any(b => b.RoomId == roomId && b.From < to && b.To > from);
        }

        public Booking Create(Booking booking)
        {
            if (HasOverlap(booking.RoomId, booking.From, booking.To))
                throw new InvalidOperationException("Booking overlaps an existing reservation.");

            return _repo.Add(booking);
        }

        public bool Cancel(int id) => _repo.Delete(id);
    }
}
